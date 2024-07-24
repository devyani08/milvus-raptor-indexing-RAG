from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

# Connect to Milvus server
connections.connect("default", host="localhost", port="19530")  # Update host and port if different

# Define schema for the collection
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
]
schema = CollectionSchema(fields, "Collection for sentence embeddings")

# Create the collection
collection_name = "sentence_embeddings"
collection = Collection(name=collection_name, schema=schema)

# Insert embeddings into Milvus
ids = list(range(len(embeddings)))  # Generate IDs for each embedding
entities = [
    ids,
    embeddings
]

collection.insert(entities)
collection.load()
