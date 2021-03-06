from flask import Blueprint
from flask_restful import Api
from api.songs.views import SongsListView, SongDetailView

song = Blueprint('song', __name__, url_prefix='/api')
song_api = Api(song)

song_api.add_resource(SongsListView, '/songs')
song_api.add_resource(SongDetailView, '/songs/<int:song_id>')