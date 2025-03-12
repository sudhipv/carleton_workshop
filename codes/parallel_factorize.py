from mpi4py import MPI
import numpy as np
import time

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
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    N = 10**5  # Increased number of computations
    numbers = None

    if rank == 0:
        np.random.seed(42)  # Set seed for reproducibility
        numbers = np.random.randint(10**5, 10**6, size=N)  # Generate only on root

    # Determine chunk size
    chunk_size = N // size
    local_numbers = np.zeros(chunk_size, dtype=int)

    # Synchronize and start timing
    comm.Barrier()
    start_time = time.time()

    # Scatter data across processes
    comm.Scatter(numbers, local_numbers, root=0)

    # Compute prime factors locally
    local_results = [largest_prime_factor(n) for n in local_numbers]

    # Gather results at root
    gathered_results = None
    if rank == 0:
        gathered_results = np.empty(N, dtype=int)

    comm.Gather(np.array(local_results, dtype=int), gathered_results, root=0)

    # Synchronize and end timing
    end_time = time.time()

    if rank == 0:
        print(f"Parallel Execution Time with {size} processes: {end_time - start_time:.4f} seconds")
        print(f"Example Result (first 5): {gathered_results[:5]}")

if __name__ == "__main__":
    main()
