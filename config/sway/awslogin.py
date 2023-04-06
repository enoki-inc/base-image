import os
import subprocess

if os.getenv('AWS_ACCESS_KEY') != "":
    access_key = os.getenv('AWS_ACCESS_KEY')
    secret_key = os.getenv('AWS_SECRET_KEY')
    region = os.getenv('AWS_CODECOMMIT_REGION')

    # Set AWS CLI credentials and output format
    subprocess.run(["aws", "configure", "set", "aws_access_key_id", access_key], check=True)
    subprocess.run(["aws", "configure", "set", "aws_secret_access_key", secret_key], check=True)
    subprocess.run(["aws", "configure", "set", "region", region], check=True)
    subprocess.run(["aws", "configure", "set", "output", "json"], check=True)

    # Authenticate to CodeCommit
    subprocess.run(["aws", "codecommit", "credential-helper", "approve"], check=True)

    print("Successfully logged in to AWS Code Commit in Enoki Workspace!")

else:
    print("AWS_ACCESS_KEY not set. Please set the AWS_ACCESS_KEY environment variable to log into AWS Code Commit.")
