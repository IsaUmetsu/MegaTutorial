def chapter12_1():
    from datetime import datetime
    print(str(datetime.now()))
    print(str(datetime.utcnow()))

def chapter14_1():
    from app.translate import translate
    print(translate('Hi, how are you today?'))

def chapter16_1():
    from elasticsearch import Elasticsearch
    es = Elasticsearch('http://localhost:9200')
    es.index(index='my_index', doc_type='my_index', id=1, body={'text': 'this is a test'})
    es.index(index='my_index', doc_type='my_index', id=2, body={'text': 'a second test'})
    print(es.search(index='my_index', doc_type='my_index',
        body={'query': {'match': {'text': 'this test'}}}))
    es.indices.delete('my_index')

def chapter16_2():
    from app.search import add_to_index, remove_from_index, query_index
    from app.models import Post
    for post in Post.query.all():
        add_to_index('posts', post)
    query_index('posts', 'one two three four five', 1, 100)
    query_index('posts', 'one two three four five', 1, 3)
    query_index('posts', 'one two three four five', 2, 3)
    query_index('posts', 'one two three four five', 3, 3)
# execute
chapter16_2()