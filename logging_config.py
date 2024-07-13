import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("sustainability_report.log"),
                                  logging.StreamHandler()])

# Example usage in save_emissions_data.py
import logging
from logging_config import setup_logging

setup_logging()

def save_emissions_data(data, filename='emissions_data.csv'):
    logging.info(f"Saving emissions data to {filename}")
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info("Emissions data saved successfully")

