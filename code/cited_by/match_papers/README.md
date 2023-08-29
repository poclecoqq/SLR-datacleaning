# match_papers
This directory contains the code that finds the papers that are cited more than once by another set of papers. In other words, it finds the snowballed papers that are cited more than once and included in our study. It counts, for each snowballed paper, the number of papers in the initial pool of papers that cite the snowball paper (using the dictionnary from step 2). 

**How to use**:
1. Import the output from last step (i.e. subdirectory `../cited_by`) into the subdirectory `./in` under the name of `cited_by.yaml`.
2. Import the output from the first step (i.e. subdirectory `../extract_paper_name`) into the subdirectory `./in` under the name of `papers.yaml`.
3. Run `script.py`
