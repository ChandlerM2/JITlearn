from models import Catalog
import chromadb
from pathlib import Path

# these are global paths
COLLECTION_NAME = "book_catalog"
DB_PATH = Path(__file__).parent.parent / "data" / "chroma_db"

raw_entries =[
    {
        "lookup_id": "9781835082225_ch1_s1",
        "title": "Python Machine Learning By Example",
        "chapter_name": "Getting Started with Machine Learning and Python",
        "subsection_name": "Understanding why we need machine learning",
        "domains": ["AI", "ML", "DS"],
        "bgn_page_number": 2,
        "end_page_number": 3
    },
    {
        "lookup_id": "9781835082225_ch1_s2",
        "title": "Python Machine Learning By Example",
        "chapter_name": "Getting Started with Machine Learning and Python",
        "subsection_name": "Differentiating between machine learning and automation",
        "domains": ["AI", "ML", "DS"],
        "bgn_page_number": 4,
        "end_page_number": 4
    }
]



# always resolves relative to this file's location
client = chromadb.PersistentClient(path= DB_PATH) # set up the DB client on disk and pathing
collection = client.get_or_create_collection(name = COLLECTION_NAME) # the name for the table / folder within the DB


# ingest the raw dictionary entries into the chromaDB collection
# we use the pydantic model to validate the data and then unpack it into the collection.add() method

for entry in raw_entries:
    catalog_entry = Catalog(**entry)
    collection.add(
        ids=[catalog_entry.lookup_id],
        documents=[catalog_entry.subsection_name],
        metadatas=[{
            "title": catalog_entry.title,
            "chapter_name": catalog_entry.chapter_name,
            "domains": catalog_entry.domains,
            "bgn_page_number": catalog_entry.bgn_page_number,
            "end_page_number": catalog_entry.end_page_number
        }]
    )

results = collection.get(ids=["9781835082225_ch1_s1"])
print(results)