from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import pandas as pd
from pathlib import Path
import os
from tqdm import tqdm
import time
import random


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def save_to_csv(df):
    crnt_path = Path(__file__).parent.resolve()
    out_path = crnt_path/"out"
    os.makedirs(out_path, exist_ok=True)
    df.to_csv(out_path/"res.csv", index=False)


def add_noisy_abstract(papers):
    res = []
    for _, row in tqdm(papers.iterrows(), total=len(papers)):
        if not row.isnull()['Url'] and row['Url'][-4:] != '.pdf':
            try:
                time.sleep((3+random.uniform(0, 1)))
                r = requests.get(row['Url'])
                abstract = text_from_html(r.text)
            except:
                abstract = ''
        else:
            abstract = ''
        res.append(abstract)
    return res


if __name__ == '__main__':
    crnt_dir = Path(__file__).parent.resolve()
    papers = pd.read_csv(crnt_dir/'lib_gs.csv')
    # papers = papers.iloc[0:500]
    noisy_abstracts = add_noisy_abstract(papers)
    papers['noisy_abstract'] = noisy_abstracts
    save_to_csv(papers)
