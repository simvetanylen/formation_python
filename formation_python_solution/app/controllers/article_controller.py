import json

from flask import Blueprint, Response, request

from app.services.article_service import ArticleService
from app.services.comment_service import CommentService

bp = Blueprint(__name__, __name__)


class ArticleController:

    @staticmethod
    @bp.route('/articles', methods=['POST'])
    def create():
        return Response(str(ArticleService.create(request.get_json())))

    @staticmethod
    @bp.route('/articles/<article_id>/comments', methods=['POST'])
    def comment(article_id):
        return Response(str(CommentService.create(article_id, request.get_json())))

    @staticmethod
    @bp.route('/articles/search/<word>', methods=['GET'])
    def search(word):
        return Response(json.dumps(ArticleService.search(word)))