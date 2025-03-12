from mpi4py import MPI
import numpy as np
import time

def sum_of_squares(numbers):
    """Compute sum of squares for a given array chunk."""
    return np.sum(np.square(numbers))

def main():
    comm = MPI.COMM_WORLD  # MPI communicator
    rank = comm.Get_rank()  # Process ID
    size = comm.Get_size()  # Total number of processes

    N = 10**6  # Large array
    numbers = None

    if rank == 0:
        # Root process initializes the data
        numbers = np.arange(N, dtype=int)

    # Determine chunk size for each process
    chunk_size = N // size
    local_numbers = np.zeros(chunk_size, dtype=int)

    # Start timer before scattering data
    comm.Barrier()  # Synchronize all processes
    start_time = time.time()

    # Distribute chunks to processes
    comm.Scatter(numbers, local_numbers, root=0)

    # Each process computes its part
    local_sum = sum_of_squares(local_numbers)

    # Reduce results at the root process
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    # Stop timer after reducing results
    end_time = time.time()
    
    if rank == 0:
        print(f"Parallel Execution Time with {size} processes: {end_time - start_time:.4f} seconds")
        print(f"Result: {total_sum}")  # Should match serial result

if __name__ == "__main__":
    main()
