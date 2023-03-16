# Local imports
from utils import save_to_yaml
from scrapper import extract_papers_titles


def main():
    papers_name = [
        'Sudowoodo: Contrastive Self-supervised Learning for Multi-purpose Data Integration and Preparation']
    titles = extract_papers_titles(papers_name)
    save_to_yaml(titles, 'titles.yaml')


if __name__ == '__main__':
    main()
