from sqlalchemy.sql import exists

from forum_service.db import get_session, session_commit
from forum_service.db.models import Forum
from forum_service.db.repository.exceptions import (
    CreateUserError, UpdateUserError, UpdateUserNotFoundError, UserNotFound,
)
from forum_service.db.repository.utils import validate_write_fields, set_write_fields
