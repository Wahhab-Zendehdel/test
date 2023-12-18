from git import Repo
import os
# Initialize a new repo in the current directory
repo = Repo.init()
# repo.config_writer().set_value('user', 'email', 'Wahhabzendehdel@gmail.com')
username = 'Wahhab-Zendehdel'
os.environ['GIT_API_KEY'] = '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'
# Add remote origin
origin = repo.create_remote('origin', f'https://{username}:{os.environ["GIT_API_KEY"]}@github.com/Wahhab-Zendehdel/test.git')

# Add file to the staging area
repo.index.add(['main.py'])

# Commit changes
repo.index.commit("git init")

# Push changes to the remote repository
origin.push(refspec='master', force=True)
