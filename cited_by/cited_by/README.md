# Cited_by
This directory contains the code we used to fetch the name of all the papers citing each snowballed paper. The output of this step is a dictionnary where the key is the snowballed paper, and the value is a list of papers citing the snowballed paper.

**How to use**:
1. Create an account on scrapper API and paste the API key in the `env.py` file (that must be created).
2. Copy the output of last step (i.e. `../extract_paper_name` directory) into the `./in/` subdirectory and name it `papers.yaml`.
3. Run `script.py`.