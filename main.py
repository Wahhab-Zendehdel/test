from git import Repo

# Initialize a new repo in the current directory
repo = Repo.init()

repo.config_writer().set_value("user.email", "Wahhabzendehdel@gmail.com").release()
repo.config_writer().set_value("user.email", "Wahhabzendehdel@gmail.com").release()

print(repo.config_reader().get_value("user.email"))
# Add remote origin
origin = repo.create_remote('origin', 'https://github.com/Wahhab-Zendehdel/test.git')

# Add file to the staging area
repo.index.add(['main.py'])

# Commit changes
repo.index.commit("git init")

# Push changes to the remote repository
origin.push(refspec='master', force=True)
