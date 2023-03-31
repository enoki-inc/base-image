import os
import subprocess

if os.getenv('GHTOKEN') != "":
    subprocess.run(["sudo apt install gh"], shell=True)
    subprocess.run(["gh auth login --with-token < " + os.getenv('GHTOKEN')], shell=True)
    print("Successfully logged in to GitHub in Enoki Workspace!")

else:
    print("GHTOKEN not set. Please set the GHTOKEN environment variable to your GitHub Personal Access Token.")
