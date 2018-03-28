import json

from flask import Response, Blueprint, request

from app.services.message_service import MessageService

bp = Blueprint(__name__, __name__)


class MessageController:
    @staticmethod
    @bp.route('/users/<user_id>/inbox', methods=['GET'])
    def get_all_inbox(user_id):
        return Response(json.dumps(MessageService.get_all_inbox(user_id)))

    @staticmethod
    @bp.route('/users/<user_id>/outbox', methods=['GET'])
    def get_all_outbox(user_id):
        return Response(json.dumps(MessageService.get_all_outbox(user_id)))

    @staticmethod
    @bp.route('/messages', methods=['POST'])
    def create():
        return Response(str(MessageService.create(request.get_json())))
