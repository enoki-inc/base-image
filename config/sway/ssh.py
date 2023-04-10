import os
import subprocess

ssh_public_key = os.getenv('SSH_PUBLIC_KEY')
ssh_private_key = os.getenv('SSH_PRIVATE_KEY')
ssh_user = os.getenv('SSH_USER')
ssh_host = os.getenv('SSH_HOST')

if ssh_private_key and ssh_user and ssh_host:
    # Create .ssh directory if it doesn't exist
    ssh_dir = os.path.expanduser('~/.ssh')
    os.makedirs(ssh_dir, exist_ok=True)

    # Write public key to authorized_keys file
    if ssh_public_key:
        authorized_keys_path = os.path.join(ssh_dir, 'authorized_keys')
        with open(authorized_keys_path, 'a') as f:
            f.write(ssh_public_key)

    # Write private key to id_rsa file
    private_key_path = os.path.join(ssh_dir, 'id_rsa')
    with open(private_key_path, 'w') as f:
        os.chmod(private_key_path, 0o600)  # Set correct file permissions
        f.write(ssh_private_key)

    print('SSH Credentials Ingested!')
else:
    print('Missing environment variables. Please set SSH_PRIVATE_KEY, SSH_USER, and SSH_HOST.')
