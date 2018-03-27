from flask import Flask, Response

from app.controllers.user_controller import bp as user_controller
from app.controllers.message_controller import bp as message_controller
from app.controllers.inbox_controller import bp as inbox_controller
from app.controllers.outbox_controller import bp as outbox_controller
from app.controllers.notification_controller import bp as notification_controller
from app.controllers.article_controller import bp as article_controller
from app.exceptions.invalid_model_exception import InvalidModelException
from app.exceptions.item_not_found_exception import ItemNotFoundException

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(message_controller)
app.register_blueprint(inbox_controller)
app.register_blueprint(outbox_controller)
app.register_blueprint(notification_controller)
app.register_blueprint(article_controller)


@app.errorhandler(ItemNotFoundException)
def handle_item_not_found_exception(ex):
    return Response(status=404)


@app.errorhandler(InvalidModelException)
def handle_invalid_model_exception(ex):
    return Response(status=400)
