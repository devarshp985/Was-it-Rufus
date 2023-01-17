# Was-it-Rufus-
Small python script that prints info of a git repo. Info includes: Currently active branch, if there are local changes, if anything has been committed in the past week, and if the last commit author was "Rufus".

Usage:
Provide the path to a directory with an initialized git repository with the "-p" flag.
'''
python ./Was_it_Rufus.py -p "/Path/to/your/git/repo"
'''

Output:
The output of the script should look something like this...
'''
active branch: master
local changes: False
recent commit: False
blame Rufus: False
'''

