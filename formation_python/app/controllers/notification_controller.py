import json

from flask import Response, Blueprint, request

from app.services.notification_service import NotificationService

bp = Blueprint(__name__, __name__)


class UserController:
    @staticmethod
    @bp.route('/users/<user_id>/notifications', methods=['GET'])
    def get_all(user_id):
        return Response(json.dumps(NotificationService.get_all(user_id)))


    @staticmethod
    @bp.route('/users/<user_id>/notifications', methods=['POST'])
    def create(user_id):
        return Response(str(NotificationService.create(user_id,request.get_json())))

