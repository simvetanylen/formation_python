from flask import Flask

from app.controllers.user_controller import blueprint as user_controller
from app.controllers.example import blueprint as example

app = Flask(__name__)

app.register_blueprint(example)
app.register_blueprint(user_controller)