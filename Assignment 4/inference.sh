#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --job-name="hipt"
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=10G
#SBATCH --time=04:00:00
#SBATCH --output=log/slurm-%j.out

srun \
	--no-container-entrypoint \
	--container-mounts=/data/pathology:/data/pathology \
        --container-image="doduo1.umcn.nl#clementgrisi/diag_day:entrypoint" \
		./run.sh \
			-w /data/pathology/projects/ais-cap/code/diag_day/best.pt
