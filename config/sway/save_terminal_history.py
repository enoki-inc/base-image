import os
import subprocess

team_name = os.getenv('TEAM_NAME')
workspace_name = os.getenv('WORKSPACE_NAME')
filepath = f'/home/dev/{team_name}/{workspace_name}/tmp/history.txt'
command = f"cp /home/dev/.bash_history {filepath}"

directory = os.path.dirname(os.path.expanduser(filepath))
if not os.path.exists(directory):
    os.makedirs(directory)

if not os.path.exists(os.path.expanduser(filepath)):
    # Create an empty file if it doesn't exist
    subprocess.run(["touch", os.path.expanduser(filepath)], check=True)

# Append the existing terminal commands to ~/.bash_history
subprocess.run(["bash", "-c", "history", "-a"], shell=True)
# Copy the history file to the new location
subprocess.run([command], shell=True)

print("Terminal history saved!")
