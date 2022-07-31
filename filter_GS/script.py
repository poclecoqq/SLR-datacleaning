import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('lib_gs.csv')
    search_terms = [["machine learning", "deep learning", "neural network", "neural networks", "reinforcement learning", "supervised", "unsupervised"],
                    ["data cleaning", "data cleansing", "data scrubbing", "data repairing", "data repair", "error repair", "error repairing", "confident learning", "label cleaning"]]
    special_search_terms = [['error detection'], [
        'tabular', 'table', 'tables', 'row', 'column', 'rows', 'columns']]

    matches = []
    for index, row in df.iterrows():
        category_found = []
        for keywords in search_terms:
            # A first-level search
            category_found.append(any([
                (type(row['Title']) == str and keyword in row['Title']) or
                (type(row['Abstract Note']) == str
                 and keyword in row['Abstract Note'])
                for keyword in keywords
            ]))
            # A second-level search
            for first_term in special_search_terms[0]:
                for second_term in special_search_terms[1]:
                    if type(row['Title']) == str and (first_term in row['Title'] and second_term in row['Title']):
                        category_found[-1] = True
                    if type(row['Abstract Note']) == str and (first_term in row['Abstract Note'] and second_term in row['Abstract Note']):
                        category_found[-1] = True

        matches.append(all(category_found))
    initial_len = len(df)
    df = df[matches]
    df.to_csv("res.csv", index=False)

    print(f'Total number of records: {initial_len}')
    final_len = len(df)
    perc = final_len / initial_len
    print(f'Number of record kept: {final_len} ({perc}%)')
