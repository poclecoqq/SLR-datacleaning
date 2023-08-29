# "Cited by" scripts

### Goal
Find the papers that are cited more than once by a set of papers. In our project, this script is used to find the snowballed papers that are cited more than once by our initial set of papers.

### How to use

Run the files `script.py` of the respective subdirectory in the following order:
1. `extract_paper_name`:  This directory contains the code we used to pre-process the spreadsheets exported by Notion. The output of the script is a list of papers' name for the initial pool of paper and the snowballed ones.
2. `cited_by`: This directory contains the code we used to fetch the name of all the papers citing each snowballed paper. The output of this step is a dictionnary where the key is the snowballed paper, and the value is a list of papers citing the snowballed paper.
3. `match_papers`: This directory contains the code that finds the papers that are cited more than once by another set of papers. In other words, it finds the snowballed papers that are cited more than once and included in our study. It counts, for each snowballed paper, the number of papers in the initial pool of papers that cite the snowball paper (using the dictionnary from step 2). 
