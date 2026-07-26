from backends.library.abstractions.contracts import DataResponse
from frontends.gamespy.protocols.presence_connection_manager.contracts.results import BlockListResult, BuddyListResult, GetProfileResult, LoginResult, NewUserResult


class LoginResponse(DataResponse):
    result: LoginResult


class NewUserResponse(DataResponse):
    result: NewUserResult



class BuddyListResponse(DataResponse):
    result: BuddyListResult


class BlockListResponse(DataResponse):
    result: BlockListResult


class GetProfileResponse(DataResponse):
    result: GetProfileResult
