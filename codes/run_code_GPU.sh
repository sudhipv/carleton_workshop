#!/bin/bash
#SBATCH --account=def-sponsor00
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=3
#SBATCH --time=00:10:00
##SBATCH --mem-per-cpu=3700M
#SBATCH --job-name=GPU_run
#SBATCH --output=%x-%j.out
#SBATCH --mail-user=sudhipv@cmail.carleton.ca
#SBATCH --mail-type=ALL
#SBATCH --mail-type=FAIL



nvidia-smi
