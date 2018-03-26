from flask import Flask

from app.controllers.user_controller import bp as user_controller
from app.controllers.message_controller import bp as message_controller
from app.controllers.inbox_controller import bp as inbox_controller
from app.controllers.outbox_controller import bp as sendbox_controller
from app.controllers.notification_controller import bp as notification_controller

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(message_controller)
app.register_blueprint(inbox_controller)
app.register_blueprint(sendbox_controller)
app.register_blueprint(notification_controller)