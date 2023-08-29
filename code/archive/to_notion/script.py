import pandas as pd
import pathlib
import os


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
    df = pd.read_csv('in.csv')
    df = filter_to_notion(df)

    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)

    df.to_csv(out_path/"out.csv", index=False)
