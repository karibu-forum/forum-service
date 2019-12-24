
from forum_service.db.repository.exceptions import *


class CreateCommentError(CreateError):
    pass

class CommentNotFoundError(NotFoundError):
    pass

