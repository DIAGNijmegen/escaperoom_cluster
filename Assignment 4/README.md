# Assignment 4

Participants should start by killing their previous job. They will then get a `inference.py` script, a `run.sh` script and a template bash script that they will use to kick off a non-interactive job that runs inference (`inference.sh`).

They have to update their Dockerfile to add an entrypoint that excecutes the `run.sh` file:

```Dockerfile
FROM doduo1.umcn.nl/uokbaseimage/diag:tf2.8-pt1.10-v2

#### Set /home/user as working directory
WORKDIR /home/user

#### COPY requirements
COPY requirements.txt .

#### Install requirements
RUN pip3 install -r requirements.txt

#### Copy inference script
COPY inference.py .

#### Configure Docker entrypoint
COPY run.sh .
ENTRYPOINT ["/bin/bash", "run.sh"]
```

:warning: Just like the `data.ipynb` file at assignment 2, the `inference.py` expects the `wholeslidedata` package to be installed. It's not in the `requirements.txt` file. They either need to update the requirements, or add a line in the Dockerfile to install `wholeslidedata`. If they don't do it, their inference docker will not run successfully!

This script will run inference with the model weights they saved at assignment 3. They need to update the script `inference.sh` to add:
* the docker image they pushed at assignment 1
* mount the directory where the training data is stored : `/data/pathology/users/clement/diag_day/data`

The `inference.py` file expects the path to the model weights, and produces a `submission.csv`. By default it will be saved in the container working directory. They need to copy it to one of the shares (Blissey/Chansey) as they will need to push it to their github repository. This should be handled inside `inference.sh`.

## Pass the assignment

The assignment is passed once they push the updated Dockerfile to their github repository, together with the `submission.csv`. We will hand out their AUC on the test set to finish the assignment.
