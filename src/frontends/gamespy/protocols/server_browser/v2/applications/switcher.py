from typing import TYPE_CHECKING, Optional, cast
from frontends.gamespy.library.abstractions.switcher import SwitcherBase
from frontends.gamespy.protocols.server_browser.aggregates.exceptions import (
    ServerBrowserException,
)
from frontends.gamespy.protocols.server_browser.v2.abstractions.handlers import (
    CmdHandlerBase,
)
from frontends.gamespy.protocols.server_browser.v2.aggregations.enums import (
    RequestType,
    ServerListUpdateOption,
)
from frontends.gamespy.protocols.server_browser.v2.aggregations.exceptions import SBException
from frontends.gamespy.protocols.server_browser.v2.applications.client import Client
from frontends.gamespy.protocols.server_browser.v2.applications.handlers import (
    P2PGroupRoomListHandler,
    SendMessageHandler,
    ServerFullInfoListHandler,
    UpdateServerInfoHandler,
    ServerMainListHandler,
)
from frontends.gamespy.protocols.server_browser.v2.contracts.requests import (
    SendMessageRequest,
    ServerInfoRequest,
    ServerListRequest,
)


class Switcher(SwitcherBase):
    _raw_request: bytes
    _client: Client

    def _process_raw_request(self) -> None:
        if len(self._raw_request) < 4:
            raise SBException("Invalid request")
        name = self._raw_request[2]
        if name not in RequestType:
            self._client.log_debug(f"Request: {name} is not a valid request.")
            return

        self._requests.append((RequestType(name), self._raw_request))

    def _create_cmd_handlers(
        self, name: int, raw_request: bytes
    ) -> CmdHandlerBase | None:
        req = raw_request
        if TYPE_CHECKING:
            self._client = cast(Client, self._client)
        match name:
            case RequestType.SERVER_LIST_REQUEST:
                handler = self.__check_update_option(req)
                return handler
            case RequestType.SERVER_INFO_REQUEST:
                return UpdateServerInfoHandler(self._client, ServerInfoRequest(req))
            case RequestType.SEND_MESSAGE_REQUEST:
                return SendMessageHandler(self._client, SendMessageRequest(req))
            case _:
                return None

    def __check_update_option(self, request: bytes) -> CmdHandlerBase:
        """
        check update option and create handler
        """
        parsed_request = ServerListRequest(request)
        parsed_request.parse()
        update_option = parsed_request.update_option

        if update_option & ServerListUpdateOption.P2P_GROUP_ROOM_LIST:
            return P2PGroupRoomListHandler(self._client, parsed_request)
        elif update_option & ServerListUpdateOption.SERVER_FULL_INFO_LIST:
            return ServerFullInfoListHandler(self._client, parsed_request)
        else:
            return ServerMainListHandler(self._client, parsed_request)

    @staticmethod
    def get_update_option(raw_request: bytes) -> ServerListUpdateOption:
        try:
            req = ServerListRequest(raw_request)
            req.parse()
            return req.update_option
        except Exception:
            return ServerListUpdateOption(0)
