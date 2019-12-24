# from sqlalchemy.orm.exc import NoResultFound

# from forum_service.db import get_session, session_commit
# from forum_service.db.models import Comment
# from forum_service.db.repository.utils import validate_write_fields, set_write_fields
# from forum_service.db.repository.comment.exceptions import CreateCommentError, CommentNotFoundError

# # TODO write instance or id method


# def get_comment(id):
#     session = get_session()
#     try:
#         comment = session.query(Comment).filter_by(id=id).one()
#     except NoResultFound:
#         raise CommentNotFoundError()
#     return comment


# def create_comment():
#     # these might not be required?
#     assert content and author_id and forum_id

#     with session_commit(exception=CreateCommentError) as session:
#         comment = Comment(
#         )
#         session.add(comment)
#     return comment


# def update_comment(comment_id, **fields):
#     pass

