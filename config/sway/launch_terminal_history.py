import subprocess
import os

team_name = os.getenv('TEAM_NAME')
workspace_name = os.getenv('WORKSPACE_NAME')

# Saving the contents of history.txt to the ash_history file
save_command = "cp " + 'home/dev/' + team_name + '/' + workspace_name + '/tmp/history.txt ' + 'home/dev/.bash_history'
subprocess.run([save_command], shell=True)

# Reloading the bash_history file

subprocess.run(["bash", "-c", "history", "-a"], shell=True)
subprocess.run(["bash", "-c", "history", "-r"], shell=True)

print("Terminal history loaded!")
