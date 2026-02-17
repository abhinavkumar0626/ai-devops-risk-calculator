import subprocess
import json

def get_git_stats():
    diff = subprocess.check_output(
        ["git", "diff", "--shortstat", "HEAD~1"]
    ).decode()

    return diff

if __name__ == "__main__":
    print(get_git_stats())
