from flask import Flask

from app.controllers.example import blueprint as example

app = Flask(__name__)

app.register_blueprint(example)
