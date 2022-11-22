import pandas as pd
import pathlib
import os


def filter_papers(papers, search_terms=[], special_search_terms=[]):
    """
    Filters out papers which are not matched by a given search query,
    if the search is performed in the abstract and title.
    Arguments:
        search_terms: first-level search terms of OR clauses joines by AND clauses
        special_search_terms: second-level OR clause in the second OR clause of our query (for the ("error detection" AND (tab* OR cell* OR row*)))
    Return: Papers that match a given query
    """
    matches = []
    for _, row in papers.iterrows():
        category_found = []
        for keywords in search_terms:
            # A first-level search
            category_found.append(any([
                (type(row['Title']) == str and keyword in row['Title']) or
                (type(row['Abstract Note']) == str
                 and keyword in row['Abstract Note'])
                for keyword in keywords
            ]))
        # # A second-level search
        for first_term in special_search_terms[0]:
            for second_term in special_search_terms[1]:
                # If there is any match with the ML category
                if any([(type(row['Title']) == str and keyword in row['Title']) or (type(row['Abstract Note']) == str and keyword in row['Abstract Note']) for keyword in search_terms[0]]):
                    # If ("error detection" AND (tab* OR cell* OR row*)) has a match in the title
                    if type(row['Title']) == str and (first_term in row['Title'] and second_term in row['Title']):
                        category_found[-1] = True
                    # If ("error detection" AND (tab* OR cell* OR row*)) has a match in the abstract
                    if type(row['Abstract Note']) == str and (first_term in row['Abstract Note'] and second_term in row['Abstract Note']):
                        category_found[-1] = True

        matches.append(all(category_found))
    papers = papers[matches]
    return papers


def save_to_csv(df):
    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)
    df.to_csv(out_path/"res.csv", index=False)


def print_stats(initial_len, final_len):
    print(f'Total number of records: {initial_len}')
    print(f'Number of record kept: {final_len}')
    print('Percentage of record kept: {:10.2f}%'.format(
        (final_len / initial_len)*100))


if __name__ == "__main__":
    papers = pd.read_csv('lib_gs.csv')
    search_terms = [*["machine learning", "deep learning", "neural network", "neural networks", "reinforcement learning", "supervised", "unsupervised"],
                    *["data cleaning", "data cleansing", "data scrubbing", "data repairing", "data repair", "error repair", "error repairing", "confident learning", "label cleaning"]]
    # These are second-level
    special_search_terms = [['error detection'], ['image', 'images', 'text',
                                                  'tabular', 'table', 'tables', 'row', 'column', 'rows', 'columns']]

    initial_len = len(papers)
    papers = filter_papers(papers, search_terms, special_search_terms)
    save_to_csv(papers)

    final_len = len(papers)
    print_stats(initial_len, final_len)
