from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date , Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models


connections.create_connection()

class PostIndex(DocType):
    text = Text()
    number = Text()

    class Meta:
        index = 'post-index'

def bulk_indexing():
    PostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Post.objects.all().iterator()))

def search(text):
    s = Search().filter('term', text=text)
    response = s.execute()
    return response