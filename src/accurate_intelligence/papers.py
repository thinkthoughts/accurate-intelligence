import arxiv
from .schemas import Paper

def load_arxiv(arxiv_id: str) -> Paper:
    search = arxiv.Search(id_list=[arxiv_id])
    result = next(search.results())
    return Paper(
        title=result.title,
        authors=[str(a) for a in result.authors],
        abstract=result.summary,
    )
