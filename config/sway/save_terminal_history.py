import os
import subprocess

team_name = os.getenv('TEAM_NAME')
workspace_name = os.getenv('WORKSPACE_NAME')
filepath = '~/' + team_name + '/' + workspace_name + '/tmp/history.txt'
command = "cp ~/.bash_history " + filepath

if not os.path.exists(os.path.dirname(filepath)):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
subprocess.run(["echo test > ~/.bash_history"], shell=True)
subprocess.run([command], shell=True)
