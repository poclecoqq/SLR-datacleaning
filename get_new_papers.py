

from typing import Tuple
import pandas as pd
import pathlib
import os


def find_new_papers(file_path_old: str, file_path_new: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Given an old set of papers and a new one, find the 
    paper from the new set that are not duplicates. Returns
    both the set of papers that are duplicates and the new ones.

    Expects each paper to have a unique key.
    """
    # Read from csv
    old_papers = pd.read_csv(file_path_old)
    new_papers = pd.read_csv(file_path_new)
    # Transform the DataFrame into a dict (the other columns into a list)
    # old_papers = old_papers.set_index('Key')
    # new_papers = new_papers.set_index('Key')

    print(f'Number of old papers: {len(old_papers)}')
    print(f'Number of new papers: {len(new_papers)}\n')

    new, duplicates = [], []
    # Searching new papers in the new set of papers
    for _, val in new_papers.iterrows():
        if len(old_papers.loc[old_papers['Key'] == val['Key']]) == 0:
            new.append(val)
        else:
            duplicates.append(val)

    print(f'Number of new papers that are duplicates: {len(duplicates)}')
    print(f'Number of new papers that are not duplicates: {len(new)}')
    print('Percentage of duplicates: {:10.4f}'.format(
        len(duplicates)/len(new_papers)))

    new = pd.DataFrame(new, columns=new_papers.columns)
    duplicates = pd.DataFrame(duplicates, columns=new_papers.columns)
    return new, duplicates


def filter_to_notion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters out irrelevant columns for the
    data extraction process on Notion.
    """
    column_names = ['Name', 'Publication Year', 'Abstract Note',
                    'Author', 'Read by', 'Relevant', 'DOI', 'Item Type']
    df = df.filter(items=column_names)
    return df


if __name__ == "__main__":
    new, duplicates = find_new_papers(
        file_path_old='Exported Items-EV.csv', file_path_new="Exported Items-ieee.csv")

    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)

    new = filter_to_notion(new)
    duplicates = filter_to_notion(duplicates)

    new.to_csv(out_path/"new.csv", index=False)
    duplicates.to_csv(out_path/"duplicates.csv", index=False)
