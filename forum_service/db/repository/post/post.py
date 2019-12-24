from sqlalchemy.orm.exc import NoResultFound

from forum_service.db import get_session, session_commit
from forum_service.db.models import Post
from forum_service.db.repository.utils import validate_write_fields, set_write_fields
from forum_service.db.repository.post.exceptions import CreatePostError, PostNotFoundError

# TODO write instance or id method


def get_post(id):
    session = get_session()
    try:
        post = session.query(Post).filter_by(id=id).one()
    except NoResultFound:
        raise PostNotFoundError()
    return post


def create_post(title, content=None, author_id=None, forum_id=None):
    # these might not be required?
    assert content and author_id and forum_id

    with session_commit(exception=CreatePostError) as session:
        post = Post(
            title=title,
            content=content,
            author_id=author_id,
            forum_id=forum_id
        )
        session.add(post)
    return post


def update_post(post_id, **fields):
    pass

