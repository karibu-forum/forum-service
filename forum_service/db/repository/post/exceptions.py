from forum_service.db.repository.exceptions import *


class CreatePostError(CreateError):
    pass

class PostNotFoundError(NotFoundError):
    pass

