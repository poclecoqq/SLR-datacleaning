import pandas as pd
import pathlib
import os


def save_to_csv(df):
    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)
    df.to_csv(out_path/"test.csv", index=False)


def print_stats(old_papers, new_papers, new_papers_gs, merged_df):
    x, y, z = len(old_papers), len(new_papers), len(new_papers_gs)
    print(f'Total number of papers: {x}+{y}+{z}={x+y+z}')
    print(
        f'Final size: {len(merged_df)} (duplicates: {1-(len(merged_df)/(x+y+z))})')

    n_to_filter = len(merged_df[merged_df['Relevant'].isnull()])
    print(f'Number of papers to filter: {n_to_filter}')


def merge_dataframes(left, right):
    """

    """
    df = pd.merge(left, right, on="Key", how="outer",
                  suffixes=["-left", "-right"])

    column_names = ['Title', 'Publication Year', 'Abstract Note',
                    'Author', 'Read by', 'Relevant', 'DOI', 'Item Type', 'Key']
    res = {}
    for column_name in column_names:
        if f'{column_name}-left' in df.columns and f'{column_name}-right' in df.columns:
            res[column_name] = df[f'{column_name}-left'].fillna(
                df[f'{column_name}-right'])
        elif f'{column_name}-left' in df.columns:
            res[column_name] = df[f'{column_name}-left']
        elif f'{column_name}-right' in df.columns:
            res[column_name] = df[f'{column_name}-right']
        elif column_name in df.columns:
            res[column_name] = df[column_name]

    res = pd.DataFrame(res)
    res = res.filter(items=column_names)
    return res


if __name__ == "__main__":
    crnt_path = pathlib.Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    # Papers stored on Notion from the search performed in June
    old_papers = pd.read_csv(crnt_path/"old_papers_kept.csv")
    # Papers obtained on Jul 29 on every DB except Google Scholar
    new_papers = pd.read_csv(crnt_path/"new.csv")
    # new_papers = filter_to_notion(new_papers)
    # Papers obtained on Jul 29 on Google Scholar
    new_papers_gs = pd.read_csv(crnt_path/"gs_filtered_papers.csv")
    # new_papers_gs = filter_to_notion(new_papers_gs)
    # Merge and filter out columns (columns from the left dataframe are kept)
    df = merge_dataframes(old_papers, new_papers)
    # df = pd.merge(old_papers, new_papers, on="Key",
    #               how="outer", suffixes=[None, "-remove"])
    # df = filter_to_notion(df)
    df = merge_dataframes(df, new_papers_gs)
    # df = pd.merge(df, new_papers_gs, on="Key",
    #               how="outer", suffixes=[None, "-remove"])
    # df = filter_to_notion(df)

    save_to_csv(df)
    print_stats(old_papers, new_papers, new_papers_gs, df)
