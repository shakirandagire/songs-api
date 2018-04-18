from flask import Blueprint
from flask_restful import Api
from api.auth.views import RegisterView

user = Blueprint('user', __name__, url_prefix='/api')
register_api = Api(user)

register_api.add_resource(RegisterView, '/register')
# song_api.add_resource(SongDetailView, '/songs/<int:song_id>')