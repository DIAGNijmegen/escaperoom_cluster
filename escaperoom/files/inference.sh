#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --job-name="inference"
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=10G
#SBATCH --time=04:00:00

srun \
	--no-container-entrypoint \
	--container-mounts=? \
        --container-image=? \
		./run.sh \
			-w /path/to/model_weights.pt
