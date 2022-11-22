

from typing import Tuple
import pandas as pd
import pathlib
import os


def find_unique_and_duplicate_papers(file_path_ref_papers: str, file_path_papers: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Given two sets of papers, returns the duplicates and uniques from one set of paper.
    Arguments:
        file_path_papers: File path to the papers that are splitted in two categries: duplicates and uniques
        file_path_ref_papers: File path to the papers that are referenced two detect duplicates in the first set of papers
    Returns:
        uniques, duplicates

    Expects each paper to have a unique key.
    """
    # Read from csv
    ref_paper_set = pd.read_csv(file_path_ref_papers)
    paper_set = pd.read_csv(file_path_papers)

    print(f'Number of papers in the ref set: {len(ref_paper_set)}')
    print(f'Number of papers in the main set: {len(paper_set)}\n')

    uniques, duplicates = [], []
    # Searching new papers in the new set of papers
    for _, val in paper_set.iterrows():
        if len(ref_paper_set.loc[ref_paper_set['Key'] == val['Key']]) == 0:
            uniques.append(val)
        else:
            duplicates.append(val)

    print(f'Number of duplicates: {len(duplicates)}')
    print(f'Number of uniques: {len(uniques)}')
    print('Percentage of duplicates: {:10.2f}%'.format(
        (len(duplicates)/len(paper_set)*100)))

    uniques = pd.DataFrame(uniques, columns=paper_set.columns)
    duplicates = pd.DataFrame(duplicates, columns=paper_set.columns)
    return uniques, duplicates


def filter_to_notion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters out irrelevant columns for the
    data extraction process on Notion.
    """
    column_names = ['Title', 'Publication Year', 'Abstract Note',
                    'Author', 'Read by', 'Relevant', 'DOI', 'Item Type', 'Key']
    df = df.filter(items=column_names)
    return df


if __name__ == "__main__":
    uniques, duplicates = find_unique_and_duplicate_papers(
        file_path_ref_papers='2-old.csv', file_path_papers="aug-10-db.csv")

    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)

    uniques = filter_to_notion(uniques)
    duplicates = filter_to_notion(duplicates)

    uniques.to_csv(out_path/"uniques.csv", index=False)
    duplicates.to_csv(out_path/"duplicates.csv", index=False)
