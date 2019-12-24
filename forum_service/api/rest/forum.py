from flask import Blueprint, jsonify, request
from forum_service.db.session import get_session, session_commit
from forum_service.app.redis import redis_conn
from forum_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError

forum_api = Blueprint('forum', __name__)


@forum_api.route('/ping', methods=['GET'])
def test():
    return 'pong', 200


@forum_api.route('/forum/get', methods=['GET'])
def forum_get():
    return 'pong', 200


@forum_api.route('/forum/create', methods=['Post'])
def forum_create():
    return 'pong', 200
