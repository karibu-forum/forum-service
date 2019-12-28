from flask import Blueprint, jsonify, request
from forum_service.db.session import get_session, session_commit
from forum_service.api.rest.exceptions import BadRequestError, ResourceNotFoundError

post_api = Blueprint('post', __name__)


@post_api.route('/posts/<string:post_id>', methods=['GET'])
def post_get(post_id):
    pass


@post_api.route('/posts/create', methods=['Post'])
def post_create():
    pass
