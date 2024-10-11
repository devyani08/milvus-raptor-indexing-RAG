from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType

connections.connect("default", host="localhost", port="19530")

def setup_milvus_collection():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),  # Adjust dim based on your model
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
        FieldSchema(name="metadata", dtype=DataType.VARCHAR, max_length=65535)
    ]
    schema = CollectionSchema(fields, "Textbook chunks collection")
    collection = Collection("textbook_chunks", schema)
    
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 1024}
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    return collection

# Example usage
collection = setup_milvus_collection()
print(f"Created Milvus collection: {collection.name}")

# Insert data
data = [
    [embedding.tolist() for embedding in embeddings],  # embeddings
    chunks,  # original text chunks
    [f"{{\"book_id\": 1, \"page\": {i+1}}}" for i in range(len(chunks))]  # metadata
]
collection.insert(data)
print(f"Inserted {collection.num_entities} entities into Milvus")