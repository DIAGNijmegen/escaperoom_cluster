# Assignment 2

We provide each participant with a template bash script that they will use to submit a job on the cluster. They will have to update the script to add:
* the docker image they pushed at assignment 1
* mount the directory where the training data is stored : `/data/pathology/users/clement/diag_day/data`.

They should start the job with either:
* a combination of `screen` and `srun`
* using `sbatch` and attaching the running container to VSCode

They will have to run the `data.ipynb` notebook that does some basic data analyss and outputs a label distribution plot. To be able to run the notebook, they’ll need one additional package that is not in the docker. They can simply pip install it.

## Pass the assignment

The assignment is passed once they push the label distribution plot to their github repository.