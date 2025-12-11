import graphene
from music.models import Artist, Album, Song
# استيراد الأنواع من الملف المجاور types.py
from .types import ArtistType, AlbumType, SongType

class Query(graphene.ObjectType):
    # Queries
    all_artists = graphene.List(ArtistType)
    artist_by_id = graphene.Field(ArtistType, id=graphene.Int())
    all_albums = graphene.List(AlbumType)
    all_songs = graphene.List(SongType)

    #   Resolvers
    def resolve_all_artists(root, info):
        return Artist.objects.all()

    def resolve_artist_by_id(root, info, id):
        try:
            return Artist.objects.get(pk=id)
        except Artist.DoesNotExist:
            return None

    def resolve_all_albums(root, info):
        return Album.objects.all()

    def resolve_all_songs(root, info):
        return Song.objects.all()