import pandas as pd
import pathlib
import os


def filter_papers(papers: pd.DataFrame):
    matches = []
    match_criteria = []
    ml_keywords = ["machine learning", "deep learning", "neural network",
                   "neural networks", "reinforcement learning", "supervised", "unsupervised"]
    data_cleaning_keywords = ["data cleaning", "data cleansing", "data scrubbing", "data repairing",
                              "data repair", "error repair", "error repairing", "confident learning", "label cleaning"]
    error_detection_keywords = (['error detection'], [
        'image', 'images', 'text', 'tabular', 'table', 'tables', 'row', 'column', 'rows', 'columns'])

    for _, row in papers.iterrows():
        has_matched = False
        match_criterion = 0
        # MATCH: ml + data cleaning. FIELD: title
        if does_match_title(row, ml_keywords) and \
                does_match_title(row, data_cleaning_keywords):
            has_matched = True
            match_criterion = 1
        # MATCH: ml + data cleaning. FIELD: abstract
        elif does_match_abstract(row, ml_keywords) and \
                does_match_abstract(row, data_cleaning_keywords):
            has_matched = True
            match_criterion = 2
        # MATCH: ml + error detection. FIELD: title
        elif does_match_title(row, ml_keywords) and \
                does_match_title(row, error_detection_keywords[0]) and \
            does_match_title(row, error_detection_keywords[1]):
            has_matched = True
            match_criterion = 3
        # MATCH: ml + error detection. FIELD: abstract
        elif does_match_abstract(row, ml_keywords) and \
                does_match_abstract(row, error_detection_keywords[0]) and \
            does_match_abstract(row, error_detection_keywords[1]):
            has_matched = True
            match_criterion = 4
        matches.append(has_matched)
        match_criteria.append(match_criterion)

    papers['match_criteria'] = match_criteria
    return papers[matches]


def does_match_title(row, keywords):
    """
    Given a row (a paper metadata) and some keywords,
    """
    matches = False
    for keyword in keywords:
        matches = matches or (
            type(row['Title']) == str and keyword in row['Title'])
    return matches


def does_match_abstract(row, keywords):
    """
    Given a row (a paper metadata) and some keywords,
    """
    matches = False
    for keyword in keywords:
        matches = matches or (
            type(row['Abstract Note']) == str and keyword in row['Abstract Note'])
    return matches


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

    initial_len = len(papers)
    papers = filter_papers(papers)
    save_to_csv(papers)

    final_len = len(papers)
    print_stats(initial_len, final_len)
