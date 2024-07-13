import pandas as pd

def analyze_emissions(log_file):
    data = pd.read_csv(log_file)
    summary = data.describe()
    print(summary)
    # Add more analysis as needed

if __name__ == "__main__":
    analyze_emissions('emissions.csv')
