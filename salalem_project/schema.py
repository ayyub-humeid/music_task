import graphene
import music.SchemaApi.queries
import music.SchemaApi.mutations

# Queries
class Query(music.SchemaApi.queries.Query, graphene.ObjectType):
    pass

# Mutations
class Mutation(music.SchemaApi.mutations.Mutation, graphene.ObjectType):
    pass
    
#  ـ final definition  Schema 
schema = graphene.Schema(query=Query, mutation=Mutation)