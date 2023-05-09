import urllib.parse
import os
import subprocess

# Get the GITPOD_SSH_TOKEN environment variable
ssh_token = os.getenv('GITPOD_SSH_TOKEN')

if ssh_token != "":
    # Define the special characters that need to be URL-encoded
    special_chars = [' ', '#', '$', '&', '+', ',', '/', ':', ';', '=', '?', '[', ']']

    # Replace each special character with its URL-encoded value, except for the "@" character
    for char in special_chars:
        if char != '@':
            ssh_token = ssh_token.replace(char, urllib.parse.quote(char))

    # Construct the VSCode remote-SSH URI with the encoded SSH token
    remote_ssh_uri = "vscode-remote://ssh-remote+" + ssh_token + "/"

    # Launch VSCode with the remote-SSH URI
    subprocess.run(["code", "--no-sandbox", "--folder-uri", remote_ssh_uri])
else:
    print("GITPOD_SSH_TOKEN environment variable is not set.")
