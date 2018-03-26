import json

from flask import Blueprint, Response, request

from app.services.message_service import MessageService

bp = Blueprint(__name__, __name__)


class MessageController:

    @staticmethod
    @bp.route('/messages', methods=['POST'])
    def create():
        return Response(str(MessageService.create(request.get_json())))
