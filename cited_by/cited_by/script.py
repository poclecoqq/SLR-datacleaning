# Local imports
from utils import save_to_yaml, load_yaml
from scrapper import extract_papers_titles


def main():
    papers_name = load_yaml("papers.yaml")["snowball"]
    titles = extract_papers_titles(papers_name)
    save_to_yaml(titles, "titles.yaml")


if __name__ == "__main__":
    main()
