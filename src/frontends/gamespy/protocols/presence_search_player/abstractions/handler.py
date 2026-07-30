from frontends.gamespy.library.abstractions.handler import CmdHandlerBase as CHB
from frontends.gamespy.protocols.presence_search_player.abstractions.contracts import RequestBase
from frontends.gamespy.protocols.presence_search_player.applications.client import Client
from frontends.gamespy.protocols.presence_search_player.aggregates.exceptions import GPException


class CmdHandlerBase(CHB):
    def __init__(self, client: Client, request: RequestBase) -> None:
        assert issubclass(type(request), RequestBase)
        assert isinstance(client, Client)
        super().__init__(client, request)

    def _handle_exception(self, ex: Exception) -> None:
        if isinstance(ex, GPException):
            if hasattr(self, "_request") and self._request and hasattr(self._request, "operation_id"):
                ex.operation_id = self._request.operation_id
            self._client.send(ex)
        super()._handle_exception(ex)
