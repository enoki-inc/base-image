import os
import subprocess

subprocess.run(["echo 'dev' | sudo -S mv /" + os.getenv('TEAM_NAME') + " /home/dev"], shell=True)
subprocess.run(["echo 'dev' | sudo -S chmod ugo+rwx /home/dev/" + os.getenv('TEAM_NAME') + "/" + os.getenv('WORKSPACE_NAME')], shell=True)
