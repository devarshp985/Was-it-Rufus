# Was-it-Rufus-
Small python script that prints info of a git repo. Info includes: Currently active branch, if there are local changes, if anything has been committed in the past week, and if the last commit author was "Rufus".

## Usage with shell script:
On a maxOS/Linux platform, simply run the shell script with a provided path to a directory containing a git repository. On Windows, run the same command in a Bash shell. 
```
sh Was_it_Rufus.sh "/Path/to/your/git/repo"
```

## Usage with python interpreter:
To run the script manually using Python, use the ```python``` command to run the script and provide the path to your git repository using the ```-p``` argument flag.
```
python ./Was_it_Rufus.py -p "/Path/to/your/git/repo"
```

## Output:
If you do not have the required python packages installed, the shell script will automatically install them and run the python program. If you are running the script manually using the ```python``` command, you may need to manually install the required python packages, refer to "Requirements" section for instructions.
The output of the script should look something like this... 
```
active branch: master
local changes: False
recent commit: False
blame Rufus: False
```

## Requirements:
Latest version of GitPython will be required to run the program. To install, run:
```
pip install GitPython
```
