import json

from flask import Response, Blueprint, request

from app.services.article_service import ArticleService

bp = Blueprint(__name__, __name__)


class ArticleController:

    @staticmethod
    @bp.route('/articles', methods=['POST'])
    def create():
        return Response(str(ArticleService.create(request.get_json())))
