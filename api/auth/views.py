from flask import request,jsonify,make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import user_args, user_id_arg
from .models import Users

class RegisterView(Resource):
    @use_args(user_args, locations=('json', 'form'))
    def post(self,args):
        new_user = Users(
            email= args['email'],
            username= args['username'],
            password= args['password'],
        )
        new_user.save()
        response={'message':'User successfully registered'
            }
        return make_response(jsonify(response), 201)

class LoginView(Resource):
    @use_args(user_args, locations=('json', 'form'))
    def post(self,args):
        user = Users.query.filter_by(id= id).first()
        new_user = Users(
            username= args['username'],
            password= args['password'],
        )
        if (new_user in user):
            response={'message':'User successfully logged in'
            }
            return make_response(jsonify(response), 200)
            new_user.save()
        
        response={'message':'Wrong details'
            }
        return make_response(jsonify(response), 201)