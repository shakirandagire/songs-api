from webargs import fields, validate

songs_args ={
    #Required validations and arguments
    'title': fields.Str(required=True, validate=validate.Length(5)),
    'artist': fields.Str(required=True, validate=validate.Length(5))
}

songs_id_arg={
    'id': fields.Int()
}