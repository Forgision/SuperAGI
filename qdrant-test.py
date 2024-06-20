from qdrant_client import QdrantClient, models
import numpy as np

client = QdrantClient(
    url="http://localhost",
    port=6333,
    api_key="11zSGQhyRVr19sXZuAnJC-xx3xehyXLuI8SkeL1C89w8Ei9kJA8_7w"
)

# client.create_collection("test",
# vectors_config=models.VectorParams(size=10, distance=models.Distance.COSINE))

print(client.get_collection('test'))

client.upsert(
        collection_name="test",
        points=[
            models.PointStruct(
                id=i,
                vector=np.random.rand(10).tolist(),
            )
            for i in range(100)
        ],
    )