#!/bin/bash

#SBATCH --job-name=spark
#SBATCH --partition=broadwl
#SBATCH --output=spark.out
#SBATCH --error=spark.err
#SBATCH --ntasks=10

module load python/anaconda-2019.03
module load spark/2.4.3

export PYSPARK_DRIVER_PYTHON=/software/Anaconda3-2019.03-el7-x86_64/bin/python

spark-submit --master local[*] 7M_PySpark_Midway.py
