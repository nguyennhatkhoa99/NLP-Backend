from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('content_blueprint', 
                        __name__, 
                        url_prefix='')
blueprint_api = Api(blueprint)