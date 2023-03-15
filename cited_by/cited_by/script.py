# External libs
from scholarly import scholarly, ProxyGenerator
# Local imports
from env import API_KEY
from utils import load_pkl, save_to_pkl

# Setup web-scraper in global space
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
scholarly.use_proxy(pg)


def main():
    # papers_name = [
    #     'Sudowoodo: Contrastive Self-supervised Learning for Multi-purpose Data Integration and Preparation']
    # res = search_cited_by(papers_name)
    # save_to_pkl(res, 'raw.pkl')
    res = load_pkl('raw.pkl')
    titles = extract_titles(res)
    save_to_pkl(titles, 'titles.pkl')


def extract_titles(cited_by_dict):
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


if __name__ == '__main__':
    main()
