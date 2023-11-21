#Allows use of Windows commands
import os 
#Ask IP that is troubleshooting, wrap in while loop to allow continuous use
working = True
while(working):
  print('Enter the IP you want to troubleshoot.')
  ip = input()
  #Ping, traces and tries to find dns host 
  print('Pinging...')
  os.system('ping {ip}')
  print('Ping complete. Tracing...')
  os.system('tracert {ip}')
  print('Trace complete. Trying to find dns host...')
  os.system('nslookup {ip}')
  print('DNS Trace complete.')
  print('Press n to troubleshoot another IP. Type anything else to quit.')
  choice = input()
  if choice == 'n' or choice == 'N':
    working = True
  else:
    working = False
