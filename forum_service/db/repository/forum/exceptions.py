from forum_service.db.repository.exceptions import *


class CreateForumError(CreateError):
    pass

class ForumNotFoundError(NotFoundError):
    pass

