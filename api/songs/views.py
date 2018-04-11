from flask import request,jsonify,make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import songs_args, songs_id_arg
from .models import Songs

class SongsListView(Resource):
    @use_args(songs_args, locations=('json', 'form'))
    def post(self,args):
        new_songs = Songs(
            title= args['title'],
            artist= args['artist']
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
            song_data['artist']=song.artist

            nyimba.append(song_data)

        response={'song_items': nyimba}
        return make_response(jsonify(response), 200)

class SongDetailView(Resource):
    def get(self, song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            return make_response(jsonify({
                'message': 'No song found'
            }))
        response = {
            'songs':{
                'id': song.id,
                'title': song.title,
                'artist': song.artist
            }
        }
        return make_response(jsonify(response), 200)

    def delete(self, song_id):
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
    
    @use_args(songs_args, locations=('json', 'form'))
    def put(self, args, song_id):
        song = Songs.query.filter_by(id=song_id).first()
        if not song:
            return make_response(jsonify({
                'message': 'No song found to edit'
            }))
        song.title = args['title'],
        song.artist = args['artist']
        song.save()
        response = {
            'song':{
                'id': song.id,
                'title': song.title,
                'artist': song.artist
            }
        }
        return make_response(jsonify(response), 201)