from forum_service.lib.exceptions import BaseException


class RepositoryError(BaseException):
    pass


class NotFoundError(RepositoryError):
    pass


class MutationError(RepositoryError):
    pass


class CreateError(MutationError):
    pass


class UpdateError(RepositoryError):
    pass


class DeleteError(MutationError):
    pass
