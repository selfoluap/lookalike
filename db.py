import weaviate

client = weaviate.Client("http://localhost:8080")

schema_config = {
    'class': 'Animals',
    'vectorizer': 'img2vec-neural',
    'vectorIndexType': 'hnsw',
    'moduleConfig': {
        'img2vec-neural': {
            'imageFields': [
                'image'
            ]
        }
    },
    'properties': [
        {
            'name': 'image',
            'dataType': ['blob']
        },
        {
            'name': 'text',
            'dataType': ['string']
        }
    ]
}

#try adding the schema and receive the schemas and if error occurs, print the error message
try:
    client.schema.create({"classes": [schema_config]})
    print(client.schema.get())
except Exception as e:
    print(e)


