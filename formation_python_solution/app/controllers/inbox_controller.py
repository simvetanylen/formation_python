import json

from flask import Blueprint, Response

from app.services.message_service import MessageService

bp = Blueprint(__name__, __name__)


class InboxController:

    @staticmethod
    @bp.route('/users/<user_id>/inbox')
    def get_inbox(user_id):
        return Response(json.dumps(MessageService.get_inbox(user_id)))
