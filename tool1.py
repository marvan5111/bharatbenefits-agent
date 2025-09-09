import pandas as pd

def run(query=None):
    df = pd.read_csv("metadata.csv")

    if query:
        results = df[df['Scheme Name'].str.contains(query, case=False, na=False)]
        if not results.empty:
            return results[['Scheme Name', 'Category', 'Benefits']].to_string(index=False)
        else:
            return f"No scheme found for '{query}'. Try another keyword."
    else:
        return "Please enter a scheme name or keyword."
