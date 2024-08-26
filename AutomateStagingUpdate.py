import paramiko

def ssh_and_update(host, port, username, pem_file_path, commands):
    try:
        ssh = paramiko.SSHClient()
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        key = paramiko.RSAKey.from_private_key_file(pem_file_path)
        
        ssh.connect(hostname=host, port=port, username=username, pkey=key)
        
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(f"Executing: {command}")
            print("Output:")
            print(stdout.read().decode())
            print("Errors:")
            print(stderr.read().decode())
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    host = "ip.address"
    port = 22  # Default SSH port
    username = "username"
    pem_file_path = "/path/to/file.pem"
    
    commands = [
        "sudo apt update",
        "sudo apt install -y" 
    ]
    
    ssh_and_update(host, port, username, pem_file_path, commands)