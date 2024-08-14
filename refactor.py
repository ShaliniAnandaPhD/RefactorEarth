import os
import subprocess
from codecarbon import EmissionsTracker
from github import Github
from refactor_earth import RefactorEarth

def clone_repository(repo_url, target_dir):
    """
    Clone the target GitHub repository into a specified directory.

    Args:
        repo_url (str): The URL of the GitHub repository to clone.
        target_dir (str): The directory where the repository will be cloned.

    Raises:
        subprocess.CalledProcessError: If the cloning process fails.
    """
    try:
        print(f"Cloning repository from {repo_url} into {target_dir}...")
        # Run the Git command to clone the repository
        subprocess.run(['git', 'clone', repo_url, target_dir], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")
        raise

def calculate_initial_metrics(directory, script_name='example_script.py'):
    """
    Calculate initial energy consumption and sustainability metrics for the code.

    Args:
        directory (str): The directory containing the code to analyze.
        script_name (str): The name of the script to run for measuring metrics.

    Returns:
        dict: A dictionary containing the initial metrics, such as energy consumption and carbon emissions.

    Raises:
        FileNotFoundError: If the specified script is not found in the directory.
        subprocess.CalledProcessError: If the script execution fails.
    """
    tracker = EmissionsTracker()

    # Verify that the script exists before attempting to run it
    script_path = os.path.join(directory, script_name)
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The script {script_name} was not found in the directory {directory}.")

    try:
        print(f"Calculating initial metrics for the script {script_name}...")
        tracker.start()  # Start the emissions tracker

        # Execute the script to measure its energy consumption
        subprocess.run(['python', script_path], check=True)

        tracker.stop()  # Stop the emissions tracker

        emissions_data = tracker.final_emissions_data
        metrics = {
            'energy_consumed': emissions_data.energy_consumed,  # in kWh
            'carbon_emissions': emissions_data.emissions  # in kgCO2
        }
        print("Initial metrics calculated successfully.")
        return metrics
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing the script: {e}")
        raise
    finally:
        tracker.stop()  # Ensure the tracker is stopped even if an error occurs

def optimize_code(repo_dir, github_token):
    """
    Optimize the code in the given directory using an AI model like CodeBERT.

    Args:
        repo_dir (str): The directory containing the cloned repository.
        github_token (str): The GitHub token for accessing the repository data.

    Returns:
        dict: A dictionary containing the optimization results, such as updated energy consumption and sustainability score.

    Raises:
        ValueError: If optimization fails due to invalid input or other issues.
    """
    try:
        print("Starting the code optimization process...")
        refactor = RefactorEarth(github_token=github_token)

        # Run the optimization process using the AI model
        results = refactor.optimize_repo(repo_dir)
        print("Code optimization completed successfully.")
        return results
    except Exception as e:
        print(f"Error during code optimization: {e}")
        raise ValueError("Optimization failed. Please check the input and try again.")

def main(repo_url, github_token, script_name='example_script.py'):
    """
    Main function to orchestrate the cloning, metric calculation, and optimization processes.

    Args:
        repo_url (str): The URL of the GitHub repository to clone.
        github_token (str): The GitHub token for accessing the repository data.
        script_name (str): The name of the script to run for initial metrics calculation.
    """
    # Derive the repository name from the URL and set the target directory
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    target_dir = os.path.join(os.getcwd(), repo_name)

    try:
        # Step 1: Clone the repository
        clone_repository(repo_url, target_dir)

        # Step 2: Calculate initial metrics
        initial_metrics = calculate_initial_metrics(target_dir, script_name)
        print(f"Initial Metrics: {initial_metrics}")

        # Step 3: Optimize the code
        optimization_results = optimize_code(target_dir, github_token)
        print(f"Optimization Results: {optimization_results}")

    except Exception as e:
        print(f"An error occurred in the process: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace with actual repo URL and GitHub token
    REPO_URL = "https://github.com/user/repo.git"
    GITHUB_TOKEN = "your_github_token"
    
    main(REPO_URL, GITHUB_TOKEN)
