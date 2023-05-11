import os

# Get the environment variables
ssh_user = os.getenv('SSH_USER')
ssh_hostname = os.getenv('SSH_HOSTNAME')
ssh_port = os.getenv('SSH_PORT')

if ssh_user == "":
  quit()
else:
  # Define the folder URI for the remote-ssh connection
  folder_uri = f'vscode-remote://ssh-remote+{ssh_user}@{ssh_hostname}:{ssh_port}/'

  # Execute the command to open Visual Studio Code with the remote-ssh extension
  os.system(f'code --no-sandbox --folder-uri "{folder_uri}"')
