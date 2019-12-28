from flask import Blueprint, jsonify, request
from forum_service.db.session import get_session, session_commit
from forum_service.db.repository import forum as forum_repo
from forum_service.db.repository import exceptions as db_exceptions
from forum_service.api.rest.serializer import ForumSerializer
 
from forum_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError

forum_api = Blueprint('forum', __name__)


def get_forum_or_raise(forum_id):
    try:
        user = forum_repo.get_forum(forum_id)
    except db_exceptions.NotFoundError:
        raise ResourceNotFoundError()
    return user


@forum_api.route('/forums/<string:forum_id>', methods=['GET'])
def forum_get(forum_id):
    forum = get_forum_or_raise(forum_id)

    forum_obj = ForumSerializer(forum).data
    response = jsonify(forum_obj)
    return response


@forum_api.route('/forums/create', methods=['Post'])
def forum_create():
    data = request.json
    name = data['name']
    description = data.get('description')



@forum_api.route('/forums/<string:forum_id>/posts', methods=['GET'])
def forum_get_posts(forum_id):
    data = request.json
    return 'ok', 200