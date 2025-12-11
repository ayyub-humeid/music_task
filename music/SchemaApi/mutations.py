import graphene
from music.models import Artist
from .types import ArtistType

# 1. class to create new artist 
class CreateArtist(graphene.Mutation): 
    artist = graphene.Field(ArtistType)

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

class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()