# Assignment 2

Each participant will have to kick off a job with:
* the docker image they pushed at assignment 1
* mount the directory where the training data is stored : `/data/pathology`

They can take a look at the [dedicted documentation page](https://diagnijmegen.github.io/deepops-sol-config/running-jobs/) if they don't know where to start. They can start the job with either:
* a combination of `screen` and `srun`
* using `sbatch` and attaching the running container to VSCode

They will have to run the `data.ipynb` notebook that does some basic data analyss and outputs a label distribution plot. To be able to run the notebook, they’ll need one additional package that is not in the docker. They can simply pip install it.

## Pass the assignment

The assignment is passed once they push the label distribution plot to their github repository.
