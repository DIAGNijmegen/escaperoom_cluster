#!/bin/bash

# help
display_help()
{
   echo "Simple model inference entrypoint, by @clementgrisi"
   echo
   echo "Syntax: docker run {image_name} [-w model_weights]"
   echo "options:"
   echo "-w     path to the model weights to load."
   echo
}

# grab flags
while getopts ":w:h" opt; do
  case $opt in
    h)
      display_help
      exit 1
      ;;
    w)
      weights="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# run inference
/usr/local/bin/python3 inference.py -w "${weights}"