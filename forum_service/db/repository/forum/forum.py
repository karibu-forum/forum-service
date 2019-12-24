from sqlalchemy.orm.exc import NoResultFound

from forum_service.db import get_session, session_commit
from forum_service.db.models import Forum
from forum_service.db.repository.utils import validate_write_fields, set_write_fields
from forum_service.db.repository.forum.exceptions import CreateForumError, ForumNotFoundError

def get_forum(id):
    session = get_session()
    try:
        forum = session.query(Forum).filter_by(id=id).one()
    except NoResultFound:
        raise ForumNotFoundError()
    return forum


def get_forum_by_name(name):
    session = get_session()
    try:
        forum = session.query(Forum).filter_by(name=name).one()
    except NoResultFound:
        raise ForumNotFoundError()
    return forum()


def create_forum(name, description=None):
    with session_commit(exception=CreateForumError) as session:
        forum = Forum(
            name=name,
            description=description,
        )
        session.add(forum)
    return forum


def update_forum_description():
    pass

