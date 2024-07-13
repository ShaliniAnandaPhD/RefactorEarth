import pandas as pd

def save_emissions_data(data, filename='emissions_data.csv'):
    """
    Save emissions data to a CSV file.

    Args:
        data (list of dict): The emissions data to save. Each dictionary in the list represents a row in the CSV file, with keys as column names.
        filename (str): The name of the CSV file to save the data. Defaults to 'emissions_data.csv'.

    Returns:
        None
    """
    # Convert the data (list of dictionaries) to a DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

# Example usage
if __name__ == "__main__":
    # Sample emissions data
    emissions_data = [
        {'timestamp': '2024-07-13 12:00:00', 'energy_consumed': 10.5, 'carbon_emitted': 0.003},
        {'timestamp': '2024-07-13 12:10:00', 'energy_consumed': 8.7, 'carbon_emitted': 0.0025},
        {'timestamp': '2024-07-13 12:20:00', 'energy_consumed': 9.1, 'carbon_emitted': 0.0028},
    ]
    
    # Save the emissions data to a CSV file
    save_emissions_data(emissions_data)
