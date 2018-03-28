from flask import Flask, Response

from app.controllers.user_controller import bp as user_controller
from app.controllers.article_controller import bp as article_controller
from app.exceptions.item_not_found_exception import ItemNotFoundException

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(article_controller)


@app.errorhandler(ItemNotFoundException)
def handle_item_not_found_exception(ex):
    return Response(status=404)
