import os
import subprocess

subprocess.run(["mv /" + os.getenv('TEAM_NAME') + " /home/dev"])
subprocess.run(['chmod ugo+rwx /home/dev/' + os.getenv('TEAM_NAME') + "/" + os.getenv('WORKSPACE_NAME')])
