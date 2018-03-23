import json

from flask import Response, Blueprint, request

from app.services.user_service import UserService

blueprint = Blueprint(__name__, __name__)


class UserController:

    @staticmethod
    @blueprint.route('/users', methods=['GET'])
    def get_all():
        return Response(json.dumps(UserService.get_all()))

    @staticmethod
    @blueprint.route('/users/<user_id>', methods=['GET'])
    def get(user_id):
        return Response(json.dumps(UserService.get(user_id)))

    @staticmethod
    @blueprint.route('/users', methods=['POST'])
    def create():
        return Response(str(UserService.create(request.get_json())))

    @staticmethod
    @blueprint.route('/users/<user_id>', methods=['PUT'])
    def update(user_id):
        UserService.update(user_id, request.get_json())
        return Response()