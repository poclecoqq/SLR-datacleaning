import os
from pathlib import Path
import yaml
import json
from difflib import SequenceMatcher as SM
from collections import defaultdict


dir_path = os.path.dirname(os.path.realpath(__file__))
input_dir = Path(dir_path)/'in'
output_dir = Path(dir_path)/'out'
output_dir.mkdir(parents=True, exist_ok=True)


def save_to_json(obj, f_name):
    with open(output_dir/f_name, 'w') as f:
        json.dump(obj, f, indent=4)


def load_yaml(f_name):
    with open(input_dir/f_name, 'r') as f:
        res = yaml.safe_load(f)
    return res


def main():
    """
    Finds all the papers in our intial pool of papers that
    cite a paper in the snowballed papers.
    """
    papers = load_yaml('papers.yaml')
    papers_cs = load_yaml('cited_by.yaml')

    res = defaultdict(list)
    # For every snowballed paper
    for p_name, papers_c in papers_cs.items():
        # For each paper that cites the snowballed paper
        for paper_c in papers_c:
            # For each paper in our initial pool of papers
            for p in papers['main']:
                ratio = SM(None, paper_c, p).ratio()
                if ratio > .8:
                    res[p_name].append((p, paper_c, ratio))
    save_to_json(res, 'out.json')


if __name__ == "__main__":
    main()
