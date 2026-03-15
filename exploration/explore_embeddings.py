from src.config import COLLECTION_NAME, DB_PATH
import chromadb
from pathlib import Path

# already have data in the DB from ingest.py, so we can just query it here to explore the embeddings that have been generated for the documents
# now we are going to see the vectors


client = chromadb.PersistentClient(path= DB_PATH) # set up the DB client on disk and create the DB if it doesn't exist within the data folder
collection = client.get_or_create_collection(name = COLLECTION_NAME) # the name for the table /

results = collection.get(include=["embeddings"])

print(results)