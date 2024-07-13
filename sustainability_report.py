import os
from typing import List
from codecarbon import EmissionsTracker

def find_python_files(directory: str) -> List[str]:
    """
    Find all Python files in the given directory and its subdirectories.

    Args:
        directory (str): The root directory to start searching for Python files.

    Returns:
        List[str]: A list of full file paths for all Python files found.
    """
    python_files = []
    for root, _, files in os.walk(directory):
        python_files.extend(
            os.path.join(root, file)
            for file in files
            if file.endswith('.py')
        )
    return python_files

def execute_file(file_path: str, tracker: EmissionsTracker) -> None:
    """
    Execute a Python file while tracking emissions.

    Args:
        file_path (str): The full path to the Python file to be executed.
        tracker (EmissionsTracker): The emissions tracker object.
    """
    print(f"Running {file_path} with CodeCarbon tracking...")
    try:
        tracker.start()
        with open(file_path, 'r') as file:
            exec(file.read())
    except Exception as e:
        print(f"An error occurred while running {file_path}: {e}")
    finally:
        tracker.stop()

def run_code_files(directory: str) -> None:
    """
    Find and execute all Python files in the given directory while tracking emissions.

    Args:
        directory (str): The root directory to start searching for Python files.
    """
    python_files = find_python_files(directory)
    tracker = EmissionsTracker()
    
    for file_path in python_files:
        execute_file(file_path, tracker)

if __name__ == "__main__":
    CODE_DIRECTORY = 'path/to/RefactorEarth/RefactorEarth-main/Code Samples'
    run_code_files(CODE_DIRECTORY)
