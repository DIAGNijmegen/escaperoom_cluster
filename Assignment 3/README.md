# Assignment 3

Participants get the `train.ipynb` notebook. It trains a simple resnet18 for 1 epoch on the development dataset. They can stay in the same container that they kicked off at assignment 2. The notebook produces a `best.pt` file that holds the model weights. By default it will be saved in the container working directory. They need to copy the weights outside of the container as these will be needed for assignment 4 (running inference on the test set) For example, they can save the model checkpoint in their project folder on Blissey/Chansey. If they don’t do it, the checkpoint will be lost once the job currently running their docker is over.

## Pass the assignment

The assignment is passed once they push the model weights to their github repository.
We will doublecheck they saved the weights somewhere on the storage server.