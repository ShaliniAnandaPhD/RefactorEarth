import cupy as cp  # Importing CuPy for super-fast GPU computations
import numpy as np  # Importing NumPy for standard CPU-based computations
import time  # Importing time to measure how fast our code runs

def gpu_acceleration_example(n: int):
    """
    Demonstrates how using a GPU can massively speed up computations compared to a CPU.

    Args:
    n (int): The size of the arrays to be created and added.

    Returns:
    tuple: The result of the addition and the time it took to run.
    """
    # Create two arrays directly on the GPU
    a_gpu = cp.arange(n)  # GPU array with values from 0 to n-1
    b_gpu = cp.arange(n)  # Another GPU array with values from 0 to n-1
    
    start_time = time.time()  # Start the timer
    c_gpu = a_gpu + b_gpu  # Perform element-wise addition on the GPU
    cp.cuda.Stream.null.synchronize()  # Make sure all GPU operations are done
    
    end_time = time.time()  # Stop the timer
    return c_gpu, end_time - start_time  # Return the result and the execution time

def cpu_acceleration_example(n: int):
    """
    Demonstrates standard CPU-based computation using NumPy.

    Args:
    n (int): The size of the arrays to be created and added.

    Returns:
    tuple: The result of the addition and the time it took to run.
    """
    # Create two arrays on the CPU
    a_cpu = np.arange(n)  # CPU array with values from 0 to n-1
    b_cpu = np.arange(n)  # Another CPU array with values from 0 to n-1
    
    start_time = time.time()  # Start the timer
    c_cpu = a_cpu + b_cpu  # Perform element-wise addition on the CPU
    
    end_time = time.time()  # Stop the timer
    return c_cpu, end_time - start_time  # Return the result and the execution time

if __name__ == "__main__":
    n = 100_000_000  # We'll use a large array size to really see the difference in speed
    
    # Benchmark the GPU example to see how much faster it is
    gpu_result, gpu_time = gpu_acceleration_example(n)
    print(f"GPU Execution Time: {gpu_time:.6f} seconds")  # Print how long the GPU took
    
    # Benchmark the CPU example to compare
    cpu_result, cpu_time = cpu_acceleration_example(n)
    print(f"CPU Execution Time: {cpu_time:.6f} seconds")  # Print how long the CPU took
    
    # Calculate and print the speedup gained by using the GPU over the CPU
    speedup = cpu_time / gpu_time
    print(f"GPU Speedup: {speedup:.2f}x")

