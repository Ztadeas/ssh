import threading
import subprocess
import paramiko as par
import sys

def ssh_command(ip, user, passwd):
    client = par.SSHClient()
    try:
      client.set_missing_host_key_policy(par.AutoAddPolicy())
      client.connect(ip, username=user, password=passwd, port=22)
      print("If u want to stop ennter: stop")
      while True:
        command = input("Enter command: ")
        if command == "stop":
          sys.exit("Succesfully logged out")
        else:
          stdin, stdout, stderr = client.exec_command(command)
          print(stdout.readlines())
        
    except:
        print("Connection failed")

ssh_command("", "", "1234")
    
