from flask import Flask

from app.controllers.user_controller import bp as user_controller
from app.controllers.message_controller import bp as message_controller

app = Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(message_controller)