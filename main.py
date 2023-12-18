from git import Repo
import os
# Initialize a new repo in the current directory
repo = Repo.init()
username = 'your_user_name'
os.environ['GIT_API_KEY'] = 'your_api_key'
# Add remote origin
origin = repo.create_remote('origin', f'https://{username}:{os.environ["GIT_API_KEY"]}@github.com/your_user_name/test.git')

# Add file to the staging area
repo.index.add(['main.py'])

# Commit changes
repo.index.commit("git init")

# Push changes to the remote repository
origin.push(refspec='master', force=True)
