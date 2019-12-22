from flask import Blueprint, jsonify, request
from forum_service.db.session import get_session, session_commit
from forum_service.app.redis import redis_conn
from forum_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError
from forum_service.db.models.user import User

forum_api = Blueprint('forum', __name__)


@forum_api.route('/ping', methods=['GET'])
def test():
    return 'pong', 200
