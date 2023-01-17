import argparse
from git import Repo, exc  # Not a default library, need to install - package name: GitPython
from datetime import datetime, timedelta, timezone

def get_info(repo):
    try:
        active_branch = repo.active_branch
    except TypeError:
        print("Error while trying to determine active branch: HEAD is detached")
        return
    
    local_changes_exist = repo.is_dirty()
    last_commit = repo.head.commit  # gets commit object so we can check if it was authored in the last week
    commit_within_week = (datetime.now(timezone.utc) - last_commit.committed_datetime) < timedelta(days=7)
    blame_Rufus = last_commit.author.name == "Rufus"

    return {
        "active branch" : active_branch,
        "local changes" : local_changes_exist,
        "recent commit" : commit_within_week,
        "blame Rufus" : blame_Rufus
    }

def print_info(repo):
    info = get_info(repo)
    if not info: return
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__=="__main__":
    # Argument parser to allow for user to input directory path
    parser = argparse.ArgumentParser(
        prog= 'Was it Rufus?',
        description= "Take home for Pronto.ai - provide absolute path to a local git repository to get info on its active branch, if there are local changes, if anything has been committed in the past week, and if the last commit author was Rufus.")
    parser.add_argument('-p', '--path')
    args = parser.parse_args()

    try:
        print_info(Repo(args.path))
    except:
        exc.InvalidGitRepositoryError
        print("The directory you provided does not contain a git directory")

