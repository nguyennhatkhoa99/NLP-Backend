from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('user_blueprint', 
                        __name__, 
                        url_prefix='')
blueprint_api = Api(blueprint)