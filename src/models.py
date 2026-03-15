from pydantic import BaseModel

# this is the cookie cutter for the catalog, it will be used to create the catalog from the pdf
class Catalog(BaseModel):
    lookup_id: str
    title: str
    chapter_name: str
    subsection_name: str
    domains : list[str]
    bgn_page_number: int
    end_page_number: int

entry1 = Catalog(
    lookup_id="9781835082225_ch1_sc1",
    title="Python Machine Learning By Example",
    chapter_name="Chapter 1",
    subsection_name="1.1 What is Machine Learning?",
    domains=["Artificial Intelligence", "Data Science"],
    bgn_page_number=1,
    end_page_number=20
)

print(entry1.title)
