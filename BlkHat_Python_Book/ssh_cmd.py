"""
Simple SSH2 command sender client for use with unix/linux based environments.
- Uses Paramiko to create said client.
- Makes a Connection to the machine running ssh_server.py
- Sends a Command to the machine running ssh_server.py
"""

import paramiko

# Makes a connection to an ssh server and sends a single command
# ITS BEST TO USE SSH KEYS !!!

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    # make a connection , assuming the connection was made we run  the command
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())

if __name__ =='__main__':
    # getpass can be used to get the username from the current environment
    # here it is used to request a password
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    # we send the IP, PORT, COMMAND to be executed
    ip = input('Enter Server IP: ') or '192.168.0.107'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)