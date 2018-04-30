from webargs import fields, validate

user_args={
    #Required validations and arguments
    'email': fields.Str(required=True, validate=validate.Length(5)),
    'username': fields.Str(required=True,validate=validate.Length(5)),
    'password': fields.Str(required=True, validate=validate.Length(5)),
}

login_args={
    #Required validations and arguments
    'username': fields.Str(required=True,validate=validate.Length(5)),
    'password': fields.Str(required=True, validate=validate.Length(5)),
}

user_id_arg={
    'id': fields.Int()
}