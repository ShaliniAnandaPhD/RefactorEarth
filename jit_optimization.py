from numba import jit, prange  # Importing JIT compilation and parallel range from Numba
import numpy as np  # Importing NumPy for efficient numerical operations
import time  # Importing the time module for benchmarking

# Define a JIT-compiled function to compute the sum of integers from 0 to n-1 using parallel execution
@jit(nopython=True, parallel=True)
def compute_sum(n: int) -> int:
    """
    Compute the sum of integers from 0 to n-1 using parallel execution.

    Args:
    n (int): The upper limit of the range (exclusive).

    Returns:
    int: The computed sum of the range.
    """
    total = 0  # Initialize the total sum to 0
    # Use prange for parallel iteration over the range
    for i in prange(n):
        total += i  # Add each integer to the total sum
    return total  # Return the computed sum

# Define a JIT-compiled function to compute the sum using NumPy for efficient numerical operations
@jit(nopython=True)
def compute_sum_numpy(n: int) -> int:
    """
    Compute the sum of integers from 0 to n-1 using NumPy for efficient numerical operations.

    Args:
    n (int): The upper limit of the range (exclusive).

    Returns:
    int: The computed sum of the range.
    """
    # Use NumPy's sum and arange functions to compute the sum efficiently
    return np.sum(np.arange(n))

# Define a function to benchmark the performance of the provided function
def benchmark(func, n: int) -> None:
    """
    Benchmark the execution time of the provided function.

    Args:
    func (Callable[[int], int]): The function to benchmark.
    n (int): The input parameter to the function.

    Returns:
    None
    """
    start_time = time.time()  # Record the start time
    result = func(n)  # Execute the function with the provided input
    end_time = time.time()  # Record the end time
    # Print the result and the execution time of the function
    print(f"{func.__name__} result: {result}")
    print(f"{func.__name__} execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    n = 100_000_000  # Define the upper limit for the range, increased for better benchmarking
    # Benchmark the compute_sum function
    benchmark(compute_sum, n)
    # Benchmark the compute_sum_numpy function
    benchmark(compute_sum_numpy, n)
