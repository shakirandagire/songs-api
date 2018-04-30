from flask import Blueprint
from flask_restful import Api
from api.auth.views import RegisterView, LoginView

user = Blueprint('user', __name__, url_prefix='/api')
register_api = Api(user)
login_api = Api(user)

register_api.add_resource(RegisterView, '/register')
login_api.add_resource(LoginView, '/login')