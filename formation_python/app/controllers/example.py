import json

from flask import Response, Blueprint

blueprint = Blueprint(__name__, __name__)


@blueprint.route('/example', methods=['GET'])
def example():
    return Response(json.dumps({
        "message": "example"
    }))
