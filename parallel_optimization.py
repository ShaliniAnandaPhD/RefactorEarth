import concurrent.futures  # Importing the concurrent.futures module for parallel execution
import time  # Importing the time module for sleep and timing execution
from typing import List, Callable, Any  # Importing type annotations for better code readability and type checking

def process_task(task_id: int) -> str:
    """
    Function to simulate processing of a task.

    Args:
    task_id (int): Identifier for the task.

    Returns:
    str: A message indicating the completion of the task.
    """
    print(f"Processing task {task_id}")  # Print the task ID being processed
    time.sleep(1)  # Simulate a time-consuming task with a 1-second sleep
    return f"Task {task_id} completed"  # Return a message indicating the task is completed

def parallel_processing(tasks: List[int], worker_function: Callable[[int], Any], max_workers: int = None) -> List[Any]:
    """
    Function to process tasks in parallel using a pool of threads.

    Args:
    tasks (List[int]): A list of task identifiers to be processed.
    worker_function (Callable[[int], Any]): The function to execute for each task.
    max_workers (int, optional): The maximum number of threads to use. Defaults to None, which lets ThreadPoolExecutor decide.

    Returns:
    List[Any]: A list of results from the worker_function.
    """
    # Create a ThreadPoolExecutor to manage a pool of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Use the map method to apply the worker_function to each task in parallel
        results = list(executor.map(worker_function, tasks))
    return results  # Return the list of results from processing the tasks

if __name__ == "__main__":
    # Define a list of task IDs to be processed
    tasks = list(range(1, 11))  # Creating a list of tasks from 1 to 10

    # Record the start time of the parallel processing
    start_time = time.time()
    
    # Call the parallel_processing function with the list of tasks and the worker function
    results = parallel_processing(tasks, process_task)
    
    # Record the end time of the parallel processing
    end_time = time.time()
    
    # Print the results of each processed task
    for result in results:
        print(result)
    
    # Calculate and print the total execution time for processing all tasks
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
