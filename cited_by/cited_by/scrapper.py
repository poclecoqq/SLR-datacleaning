from scholarly import scholarly, ProxyGenerator
from env import API_KEY


# Setup web-scraper in global space
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
scholarly.use_proxy(pg)


def extract_papers_titles(papers_name):
    """
    Given a list of papers' names, fetches the papers that cites
    the given papers.
    Input:
        papers_name: a list of papers' names
    Output:
        titles: a dictionnary where the key is one of the given papers and the value
                is a list of papers' names which cite this paper
    """
    res = search_cited_by(papers_name)
    titles = extract_titles(res)
    return titles


def extract_titles(cited_by_dict):
    """
    Given the raw scholarly dictionnary, return 
    a dictionnary where only the paper's names are kept.
    """
    def extract_title(p):
        return p['bib']['title']

    res = {}
    for paper_name, papers_c in cited_by_dict.items():
        v = list(map(extract_title, papers_c))
        res[paper_name] = v

    return res


def search_cited_by(papers_name):
    """
    Finds studies that cite each study in papers_name array.
    Input:
        papers_name: A list of papers' names
    Output:
        res: A dictionnary where the key is the paper's name and the value, a list of papers that cite the paper
    """
    res = {}
    for paper_name in papers_name:
        res[paper_name] = []
        search_query = scholarly.search_pubs(paper_name)
        # I suppose the first paper is the right one
        study = next(search_query)
        s_cited_by = scholarly.citedby(study)
        # Save the info of the studies citing this study
        for s in s_cited_by:
            res[paper_name].append(s)
    return res
