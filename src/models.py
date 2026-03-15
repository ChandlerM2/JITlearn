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


# examples 
entry1 = Catalog(
    lookup_id="9781835082225_ch1_s1",
    title="Python Machine Learning By Example",
    chapter_name="Getting Started with Machine Learning and Python",
    subsection_name="Understanding why we need machine learning",
    domains= ["AI", "ML", "DS"],
    bgn_page_number=2,
    end_page_number=3
)

entry2 = Catalog( 
    lookup_id="9781835082225_ch1_s2",
    title="Python Machine Learning By Example",
    chapter_name="Getting Started with Machine Learning and Python",
    subsection_name="Differentiating between machine learning and automation",
    domains= ["AI", "ML", "DS"],
    bgn_page_number= 4,
    end_page_number= 4
)

