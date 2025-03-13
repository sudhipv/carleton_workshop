#!/bin/bash
#SBATCH --account=def-sponsor00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:20:00
##SBATCH --mem-per-cpu=3700M
#SBATCH --job-name=cnn_cpu
#SBATCH --output=%x-%j.out
#SBATCH --mail-user=sudhipv@cmail.carleton.ca
#SBATCH --mail-type=ALL
#SBATCH --mail-type=FAIL

module load python
module load mpi4py
module load scipy-stack

source ./../flow/bin/activate


python CNN.py

