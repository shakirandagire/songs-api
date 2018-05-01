from flask import request,jsonify,make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import songs_args, songs_id_arg, artist_id_arg, artist_args
from .models import Songs,Artist
from api.auth.models import Users
from functools import wraps

def authentication(func):
    """Function to handle the user authentication"""
    @wraps(func)
    def auth(*args,**kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return make_response(jsonify({"message": "No token provided, Please login"}),401)
        access_token = auth_header.split()[1]
        if access_token:
            # Attempt to decode the token and get the User ID
            user_id = Users.decode_token(access_token)
            if not isinstance(user_id, str):
                return func(*args, **kwargs)
            return make_response(jsonify({'message': user_id}),401)
        return make_response(jsonify({"message": "Please login"}),401)
    return auth


class SongsListView(Resource):
    @authentication
    @use_args(songs_args,locations=('json', 'form'))
    def post(self,args):
        new_songs = Songs(
            title= args['title'],
            artist_id=args['artist_id'],
        )
        new_songs.save()
        response={
            'messages': 'Song successfully created',
            }
        return make_response(jsonify(response), 201)

    def get(self):
        songs = Songs.query.all()
        nyimba = []
        for song in songs:
            song_data = {}
            song_data['id']=song.id
            song_data['title']=song.title
            song_data['artist']=Artist.query.filter_by(id=song.artist_id).first().name
            nyimba.append(song_data)

        response={'song_items': nyimba}
        return make_response(jsonify(response), 200)

class SongDetailView(Resource):
    def get(self,song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            return make_response(jsonify({
                'message': 'No song found'
            }))
        response = {
            'songs':{
                'id': song.id,
                'title': song.title,
                'artist': song.artist_id
            }
        }
        return make_response(jsonify(response), 200)

    @authentication
    def delete(self,song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            return make_response(jsonify({
                'message': 'No song found to delete'
            }))
        song.delete()
        response={
            'messages': 'Song successfully deleted',
            }
        return make_response(jsonify(response), 200)

    @authentication
    @use_args(songs_args, locations=('json', 'form'))
    def put(self, args, song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            return make_response(jsonify({
                'message': 'No song found to edit'
            }))
        song.title = args['title'],
        song.update()
        response = {
            'song':{
                'id': song.id,
                'title': song.title,
                'artist': song.artist_id,
            }
        }
        return make_response(jsonify(response), 200)

class ArtistListView(Resource):
    @authentication
    @use_args(artist_args, locations=('json', 'form'))
    def post(self,args):
        artist = Artist(
            name= args['name'],
        )
        artist.save()
        response={
            'messages': 'Artist successfully created',
            }
        return make_response(jsonify(response), 201)

    def get(self):
        artists = Artist.query.all()
        omuyimbi = []
        for artist in artists:
            artist_data = {}
            artist_data['id']=artist.id
            artist_data['name']=artist.name
            omuyimbi.append(artist_data)
        response={'artist': omuyimbi}
        return make_response(jsonify(response), 200)

class ArtistDetailView(Resource):
    def get(self, artist_id):
        artist = Artist.query.filter_by(id=artist_id).first()

        if not artist:
            return make_response(jsonify(
                {'message': "No artist found"}
            ))
        songs = [song.title for song in artist.songs]  # list comprehension 
        """
            songs = []
            for song in artist.songs:
                songs.append(song.title)
        """
        return make_response(jsonify(
            {
                'name': artist.name,
                'number of songs': len(artist.songs),
                'songs': songs
            }
        ))
