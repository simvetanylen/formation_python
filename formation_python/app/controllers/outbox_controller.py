import json

from flask import Blueprint, Response

from app.services.message_service import MessageService

bp = Blueprint(__name__, __name__)


class OutboxController:

    @staticmethod
    @bp.route('/users/<user_id>/outbox')
    def get(user_id):
        return Response(json.dumps(MessageService.get_outbox(user_id)))
