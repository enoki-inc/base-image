import os
import subprocess

if os.getenv('GHTOKEN') != "":
    print(os.getenv('GHTOKEN'))
    subprocess.run(['echo $GHTOKEN > /home/dev/ghtoken.txt'], shell=True)

    subprocess.run(["gh auth login --with-token < /home/dev/ghtoken.txt"], shell=True)
    print("Successfully logged in to GitHub in Enoki Workspace!")

else:
    print("GHTOKEN not set. Please set the GHTOKEN environment variable to your GitHub Personal Access Token.")
