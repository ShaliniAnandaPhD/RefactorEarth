from numba import jit, prange  # Importing JIT compilation and parallel processing tools from Numba
import numpy as np  # Using NumPy for efficient numerical computations
import time  # Importing time to measure how fast our functions run

# Why JIT Compilation?
# RefactorEarth aims to optimize and refactor Python code to be more efficient and sustainable.
# One of the key challenges in optimizing code is improving its speed and reducing its resource usage.
# JIT (Just-In-Time) compilation is a powerful tool that can help us achieve this by converting Python code
# into machine code on the fly, making it run much faster, especially for repetitive tasks.
# This is essential for RefactorEarth, as we're often dealing with large datasets and complex calculations
# that need to be performed quickly and efficiently to minimize energy consumption and carbon footprint.

# Let's start by using JIT to speed up a function that adds up all the numbers from 0 to n-1, 
# and we'll take advantage of parallel processing to make it even faster.

@jit(nopython=True, parallel=True)
def compute_sum(n: int) -> int:
    """
    Add up all the numbers from 0 to n-1 using parallel execution.

    Args:
    n (int): The upper limit of the range (exclusive).

    Returns:
    int: The total sum.
    """
    total = 0  # Start with a sum of 0
    # prange allows us to loop over the range in parallel, meaning multiple processes can add numbers at the same time.
    for i in prange(n):
        total += i  # Add each number to the total sum
    return total  # Return the final sum

# Now, let's use JIT again, but this time with NumPy, which is already designed for high performance.
@jit(nopython=True)
def compute_sum_numpy(n: int) -> int:
    """
    Add up all the numbers from 0 to n-1 using NumPy, which is the go-to library for fast numerical operations.

    Args:
    n (int): The upper limit of the range (exclusive).

    Returns:
    int: The total sum.
    """
    # NumPy's sum and arange functions do the heavy lifting here, and JIT makes them even faster.
    return np.sum(np.arange(n))

# This function will help us see how much time it takes for our functions to run.
def benchmark(func, n: int) -> None:
    """
    Measure how fast the provided function runs.

    Args:
    func (Callable[[int], int]): The function you want to test.
    n (int): The number you want to pass to the function.

    Returns:
    None
    """
    start_time = time.time()  # Start the clock
    result = func(n)  # Run the function with the input number
    end_time = time.time()  # Stop the clock
    # Print out the result and how long it took
    print(f"{func.__name__} result: {result}")
    print(f"{func.__name__} execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    n = 100_000_000  # We'll use a large number to really test the speed improvements
    # Benchmark the compute_sum function to see how fast it is
    benchmark(compute_sum, n)
    # Benchmark the compute_sum_numpy function to see how it compares
    benchmark(compute_sum_numpy, n)

