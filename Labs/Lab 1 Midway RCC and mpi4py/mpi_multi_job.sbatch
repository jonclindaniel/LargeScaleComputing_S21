#!/bin/bash

#SBATCH --job-name=mpi_multi_job
#SBATCH --ntasks=11
#SBATCH --partition=broadwl
#SBATCH --constraint=fdr

# Load Python and MPI modules
module load python/anaconda-2019.03
module load intelmpi/2018.2.199+intel-18.0

# Run the python program with mpirun, using & to run jobs at the same time
mpirun -n 1 python3 ./mpi_rand_walk.py > ./mpi_nprocs1.out &
mpirun -n 10 python3 ./mpi_rand_walk.py > ./mpi_nprocs10.out &

# Wait until all simultaneous mpiruns are done
wait
