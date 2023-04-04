import os
import subprocess

team_name = os.getenv('TEAM_NAME')
workspace_name = os.getenv('WORKSPACE_NAME')
filepath = f'~/{team_name}/{workspace_name}/tmp/history.txt'
command = f"cp ~/.bash_history {filepath}"

if not os.path.exists(os.path.dirname(filepath)):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

# Check if ~/.bash_history is empty
if os.stat(os.path.expanduser('~/.bash_history')).st_size == 0:
    # If empty, write "test" to it
    subprocess.run(["echo test > ~/.bash_history"], shell=True)

# Copy the history file to the new location
subprocess.run([command], shell=True)
