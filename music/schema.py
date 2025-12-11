import graphene
from graphene_django.types import DjangoObjectType
from .models import Artist, Album, Song

# --------------------------
# 1. (Types)
# --------------------------

# Artist
class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'birth_year', 'albums')

# Album
class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ('id', 'title', 'release_date', 'artist', 'songs')

# Song
class SongType(DjangoObjectType):
    # تعريف حقل duration يدوياً كنص لحل مشكلة الوقت
    duration = graphene.String()

    class Meta:
        model = Song
        fields = ('id', 'title', 'track_number', 'album')

    def resolve_duration(self, info):
        return str(self.duration)

# --------------------------
# 2. (Mutations)
# --------------------------

class CreateArtist(graphene.Mutation):
    artist = graphene.Field(ArtistType)

    # inputs
    class Arguments:
        name = graphene.String(required=True)
        bio = graphene.String(required=False)
        birth_year = graphene.Int(required=False)

    
    def mutate(root, info, name, bio=None, birth_year=None):
        artist = Artist.objects.create(
            name=name,
            bio=bio,
            birth_year=birth_year
        )
        return CreateArtist(artist=artist)

# --------------------------
# 3.   (Queries) and Mutations
# --------------------------

class Query(graphene.ObjectType):
    all_artists = graphene.List(ArtistType)
    artist_by_id = graphene.Field(ArtistType, id=graphene.Int())
    all_albums = graphene.List(AlbumType)
    all_songs = graphene.List(SongType)

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

# Mutation
class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()