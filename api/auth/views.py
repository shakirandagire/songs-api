from flask import request,jsonify,make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import user_args, user_id_arg, login_args
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
    @use_args(login_args, locations=('json', 'form'))
    def post(self,args):
        try:
            user = Users.query.filter_by(username=args['username']).first()
            if user and user.password_is_valid(args['password']):
                access_token = user.generate_token(user.id)
                if access_token:
                    return make_response(jsonify({'message':'User successfully logged in',
                            'access_token': access_token,
                            }), 200)   
                # User does not exist. Therefore, we return an error message
            return make_response(jsonify({'message': 'Invalid email or password, Please try again'}), 401)
        except Exception as e:
            return make_response(jsonify({'message': 'An error occured when logging in.'}), 401)
