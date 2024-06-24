import random
import time

def complex_inefficient_algorithm(matrix, target_sum):
    """
    A complex and inefficient algorithm that searches for all combinations of 
    elements in a matrix that sum up to a target value.

    This algorithm uses excessive nested loops, performs redundant calculations,
    and has poor memory management.

    Args:
    matrix (list of lists): A 2D matrix of integers
    target_sum (int): The target sum to search for

    Returns:
    list of tuples: All combinations of elements that sum up to the target
    """
    rows = len(matrix)
    cols = len(matrix[0])
    results = []

    # Outer loop to iterate through all possible starting positions
    for start_row in range(rows):
        for start_col in range(cols):
            # Middle loop to determine the size of the sub-matrix
            for sub_rows in range(1, rows - start_row + 1):
                for sub_cols in range(1, cols - start_col + 1):
                    # Inner loop to calculate the sum of each sub-matrix
                    current_sum = 0
                    elements = []
                    for i in range(start_row, start_row + sub_rows):
                        for j in range(start_col, start_col + sub_cols):
                            current_sum += matrix[i][j]
                            elements.append((i, j, matrix[i][j]))
                    
                    # Check if the current sum matches the target
                    if current_sum == target_sum:
                        # Inefficient way to check for duplicates
                        is_duplicate = False
                        for existing_result in results:
                            if set(existing_result) == set(elements):
                                is_duplicate = True
                                break
                        if not is_duplicate:
                            results.append(elements)
    
    # Inefficient sorting of results
    sorted_results = []
    while results:
        min_result = min(results, key=lambda x: x[0][0])
        sorted_results.append(min_result)
        results.remove(min_result)

    return sorted_results

def generate_large_matrix(rows, cols, min_val, max_val):
    """Generate a large matrix with random integer values."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    """Print the matrix in a formatted way."""
    for row in matrix:
        print(" ".join(f"{x:3d}" for x in row))

# Usage example
if __name__ == "__main__":
    # Generate a large matrix
    rows, cols = 20, 20
    min_val, max_val = 1, 100
    matrix = generate_large_matrix(rows, cols, min_val, max_val)

    print("Generated Matrix:")
    print_matrix(matrix)

    # Set a target sum
    target_sum = 500

    print(f"\nSearching for combinations that sum up to {target_sum}...")
    start_time = time.time()

    # Run the algorithm
    results = complex_inefficient_algorithm(matrix, target_sum)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\nFound {len(results)} combinations:")
    for combo in results[:5]:  # Print first 5 combinations
        print(f"  {combo}")
    if len(results) > 5:
        print(f"  ... and {len(results) - 5} more.")

    print(f"\nExecution time: {execution_time:.2f} seconds")

    # Memory usage estimation (very rough estimate)
    memory_usage = rows * cols * 8  # Assuming 64-bit integers
    memory_usage += len(results) * (rows * cols * 24)  # Rough estimate for results storage
    print(f"Estimated memory usage: {memory_usage / (1024*1024):.2f} MB")
