# Initialize Git in the directory (if not already initialized)
git init

# Add the file to the repository
git add hello.py

# Commit the changes
git commit -m "Add hello.py script"

# Add your GitHub repository URL as remote (replace <your_username> and <repo_name>)
git remote add origin https://github.com/<your_username>/hello-python.git

# Push the code to the repository (main branch)
git push -u origin main
