import json

from flask import Blueprint, Response, request

from app.services.message_service import MessageService

bp = Blueprint(__name__, __name__)

class MessageController:

    @staticmethod
    @bp.route('/messages', methods=['POST'])
    def create():
        return Response(str(MessageService.create(request.get_json())))

    @staticmethod
    @bp.route('/users/<user_id>/messages/inbox')
    def get_inbox(user_id):
        return Response(json.dumps(MessageService.get_inbox(user_id)))

    @staticmethod
    @bp.route('/users/<user_id>/messages/sendbox')
    def get_sendbox(user_id):
        return Response(json.dumps(MessageService.get_sendbox(user_id)))