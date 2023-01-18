#!/bin/bash

# This script will run a python script that prints info about the git respository that exists in the user-provided directory path.
# It will also install the required python libraries if they do not exist yet on the users machine

if python -c "import git" &> /dev/null; then
    :
else
    printf 'The required python packages to run this script are not installed on your system, installing now...\n'
    pip install GitPython
    printf "\nAll required packaged installed. Running script...\n\n"
fi

python Was_it_Rufus.py -p $1