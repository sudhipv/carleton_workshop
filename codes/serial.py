import time
import numpy as np

def sum_of_squares(numbers):
    """Compute sum of squares of numbers."""
    return np.sum(np.square(numbers))

def main():
    N = 10**6  # Large array for computation
    numbers = np.arange(N, dtype=int)

    start_time = time.time()  # Start timer
    result = sum_of_squares(numbers)
    end_time = time.time()  # End timer

    print(f"Serial Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")  # Ensure consistency with parallel execution

if __name__ == "__main__":
    main()
