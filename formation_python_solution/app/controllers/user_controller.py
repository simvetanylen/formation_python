import json

from flask import Response, Blueprint, request

from app.exceptions.invalid_model_exception import InvalidModelException
from app.services.user_service import UserService

bp = Blueprint(__name__, __name__)


class UserController:

    @staticmethod
    @bp.route('/users', methods=['GET'])
    def get_all():
        return Response(json.dumps(UserService.get_all()))

    @staticmethod
    @bp.route('/users/<user_id>', methods=['GET'])
    def get(user_id):
        return Response(json.dumps(UserService.get(user_id)))

    @staticmethod
    @bp.route('/users', methods=['POST'])
    def create():
        return Response(str(UserService.create(request.get_json())))

    @staticmethod
    @bp.route('/users/<user_id>', methods=['PUT'])
    def update(user_id):
        UserService.update(user_id, request.get_json())
        return Response()

    @staticmethod
    @bp.route('/users/<user_id>', methods=['DELETE'])
    def delete(user_id):
        UserService.delete(user_id)
        return Response()
