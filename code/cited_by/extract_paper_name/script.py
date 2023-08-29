import os
from pathlib import Path
import pandas
import yaml


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
input_dir = dir_path / "in"
output_dir = dir_path / "out"
output_dir.mkdir(parents=True, exist_ok=True)


def save_to_yaml(obj):
    with open(output_dir / "out.yaml", "w") as f:
        yaml.dump(obj, f, width=1000)


def standardize_names(papers):
    """
    Standardizes the papers' names (i.e. replaces \n with a space)
    """
    return list(map(lambda x: x.replace("\n", " "), papers))


def filtering_papers(papers):
    """
    Filters out papers that are excluded from our study
    """
    return papers[
        papers["Relevant"].isin(
            [
                "YES",
            ]
        )
    ]


def extract_names(papers):
    """
    Extracts the papers' names from the csv and standardizes the names
    """
    papers = filtering_papers(papers)
    papers = papers.dropna(subset=["Name"])
    papers = standardize_names(papers["Name"].tolist())
    return papers


def main():
    m_papers_names = extract_names(pandas.read_csv(input_dir / "main.csv"))
    s_papers_names = extract_names(pandas.read_csv(input_dir / "snowballing.csv"))
    res = {"main": m_papers_names, "snowball": s_papers_names}
    save_to_yaml(res)


if __name__ == "__main__":
    main()
