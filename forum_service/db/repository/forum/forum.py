from sqlalchemy.sql import exists

from forum_service.db import get_session, session_commit
from forum_service.db.models import Forum
from forum_service.db.repository.utils import validate_write_fields, set_write_fields
from forum_service.db.repository.forum.exceptions import CreateForumError

def get_forum():
    pass


def create_forum(name, description=None):
    with session_commit(exception=CreateForumError) as session:
        forum = Forum(
            name=name,
            description=description,
        )
        session.add(forum)


def update_forum_description():
    pass

