from flask import Blueprint, request, Response

from app.services.notification_service import NotificationService

bp = Blueprint(__name__, __name__)


class NotificationController:

    @staticmethod
    @bp.route('/users/<user_id>/notifications', methods=['POST'])
    def create(user_id):
        return Response(str(NotificationService.create(user_id, request.get_json())))
