import time
import numpy as np

def largest_prime_factor(n):
    """Returns the largest prime factor of a number n."""
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n  # The largest factor is stored in n

def main():
    N = 10**5  # Increase the number of computations
    np.random.seed(42)  # Set seed for reproducibility
    numbers = np.random.randint(10**5, 10**6, size=N)  # Random large numbers

    start_time = time.time()
    results = [largest_prime_factor(n) for n in numbers]  # Compute serially
    end_time = time.time()

    print(f"Serial Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Example Result (first 5): {results[:5]}")  # Print sample results

if __name__ == "__main__":
    main()
