import paramiko
import time
from getpass import getpass
import datetime
username = input('SSH User : ')
password = input('SSH Password : ')
print ('cli Configuration Automation v1.2')

DEVICE_IP_LIST = open('DEVICE_IP_LIST.txt')
for DEVICE in DEVICE_IP_LIST:
    DEVICE = DEVICE.strip()    
    print ('\n ###### Connecting to the Device ' + DEVICE +'#####\n')
    SSHSESSION = paramiko.SSHClient()
    SSHSESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSHSESSION.connect(DEVICE, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)

    DEVICE_ACCESS = SSHSESSION.invoke_shell()
    
    DEVICE_ACCESS.send(b'conf t\n')
    time.sleep(2)

    DEVICE_ACCESS.send(b'vlan 2\n')
    DEVICE_ACCESS.send(b'name 10.18.10.x/24_Client\n')
    time.sleep(2)
  
    OUTPUT = DEVICE_ACCESS.recv(65000)
    print (OUTPUT.decode('ascii'))

    SAVE_DEVICE_OUTPUT = open('NODE_' + DEVICE +('-')+ str(TIMENOW.year)+('-')+
    str(TIMENOW.month)+('-')+str(TIMENOW.day)+('.txt'), 'w')
    SAVE_DEVICE_OUTPUT.write(OUTPUT.decode('ascii'))
    SAVE_DEVICE_OUTPUT.close
    SSHSESSION.close
