# Assignment 1

We provide each participant with a template Dockerfile and a list of packages required.
They first have to update the Dockerfile with a step that install the packages listed in the `requirements.txt` file.

```Dockerfile
FROM doduo1.umcn.nl/uokbaseimage/diag:tf2.8-pt1.10-v2

#### Set /home/user as working directory
WORKDIR /home/user

#### COPY requirements
COPY requirements.txt .

#### Install requirements
RUN pip3 install -r requirements.txt
```

Then, they need to build the docker image and push it to the registry.

## Pass the assignment

The assignment is passed once they push the updated Dockerfile to their github repository.
We will doublecheck the image is available on our registry.
