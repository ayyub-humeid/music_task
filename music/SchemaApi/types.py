import graphene
from graphene_django.types import DjangoObjectType
from music.models import Artist, Album, Song

# -----------------
# Artist Type
# -----------------
class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'birth_year', 'albums')

# -----------------
# Album Type
# -----------------
class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ('id', 'title', 'release_date', 'artist', 'songs')

# -----------------
# Song Type
# -----------------
class SongType(DjangoObjectType):
    duration = graphene.String()
    
    class Meta:
        model = Song
        fields = ('id', 'title', 'track_number', 'album')

    def resolve_duration(self, info):
        return str(self.duration)