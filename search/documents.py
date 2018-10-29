from django_elasticsearch_dsl import DocType, Index
# from elasticsearch_dsl import FacetedSearch, TermsFacet
from .models import Post

posts = Index('posts')


@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields = [
            'text',
            'id',
            'number',
        ]