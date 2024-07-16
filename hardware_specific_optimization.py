import cupy as cp  # Importing CuPy for GPU-accelerated computations
import numpy as np  # Importing NumPy for CPU-based numerical operations
import time  # Importing the time module for benchmarking

def gpu_acceleration_example(n: int):
    """
    Example function to demonstrate GPU acceleration using CuPy.

    Args:
    n (int): The size of the arrays to be created and added.

    Returns:
    tuple: The result of the addition and the execution time.
    """
    a_gpu = cp.arange(n)  # Create a GPU array with values from 0 to n-1
    b_gpu = cp.arange(n)  # Create another GPU array with values from 0 to n-1
    
    start_time = time.time()  # Record the start time
    c_gpu = a_gpu + b_gpu  # Perform element-wise addition on the GPU
    cp.cuda.Stream.null.synchronize()  # Ensure all GPU operations are complete
    
    end_time = time.time()  # Record the end time
    return c_gpu, end_time - start_time  # Return the result and the execution time

def cpu_acceleration_example(n: int):
    """
    Example function to demonstrate CPU-based computation using NumPy.

    Args:
    n (int): The size of the arrays to be created and added.

    Returns:
    tuple: The result of the addition and the execution time.
    """
    a_cpu = np.arange(n)  # Create a CPU array with values from 0 to n-1
    b_cpu = np.arange(n)  # Create another CPU array with values from 0 to n-1
    
    start_time = time.time()  # Record the start time
    c_cpu = a_cpu + b_cpu  # Perform element-wise addition on the CPU
    
    end_time = time.time()  # Record the end time
    return c_cpu, end_time - start_time  # Return the result and the execution time

if __name__ == "__main__":
    n = 100_000_000  # Define the size of the arrays for benchmarking
    
    # Benchmark the GPU-accelerated example
    gpu_result, gpu_time = gpu_acceleration_example(n)
    print(f"GPU Execution Time: {gpu_time:.6f} seconds")  # Print the GPU execution time
    
    # Benchmark the CPU-based example
    cpu_result, cpu_time = cpu_acceleration_example(n)
    print(f"CPU Execution Time: {cpu_time:.6f} seconds")  # Print the CPU execution time
    
    # Calculate and print the speedup of GPU over CPU
    speedup = cpu_time / gpu_time
    print(f"GPU Speedup: {speedup:.2f}x")
