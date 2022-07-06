import base64
import paramiko
from config import key

ip = '172.0.0.1'
ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.connect(ip, username='dvannoy', key_filename='/Users/dustinvannoy/.ssh/dvannoy')
# stdin, stdout, stderr = ssh_client.exec_command('ls /')
# for line in stdout:
#     print('... ' + line.strip('\n'))
# ssh_client.close()

sftp_client = ssh_client.open_sftp()
with sftp_client.open('test.txt') as remote_file:
    for line in remote_file:
        print(line)

