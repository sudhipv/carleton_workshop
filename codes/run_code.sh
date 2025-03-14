#!/bin/bash
#SBATCH --account=def-sponsor00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --time=00:10:00
##SBATCH --mem-per-cpu=3700M
#SBATCH --job-name=mpi_parallel_factorize
#SBATCH --output=%x-%j.out
#SBATCH --mail-user=sudhipv@cmail.carleton.ca
#SBATCH --mail-type=ALL
#SBATCH --mail-type=FAIL

module load python
module load mpi4py
module load scipy-stack

### For running the serial code
# python serial.py
# python serial_factorize.py

### For running the parallel MPI code
# mpiexec -n 8 python parallel.py
mpiexec -n 2 python parallel_factorize.py

