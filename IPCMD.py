#Allows use of Windows commands
import os 
#Ask IP that is troubleshooting
working = True
while(working):
  print('Enter the IP you want to ping and trace.')
  ip = input()
  #Ping, traces and tries to find dns host 
  print('Pinging...')
  os.system(f'ping {ip}')
  print('Ping complete. Tracing...')
  os.system(f'tracert {ip}')
  print('Trace complete. Trying to find dns host...')
  os.system(f'nslookup {ip}')
  print('DNS Trace complete.')
  print('Press n to troubleshoot another IP. Type anything else to quit.')
  choice = input()
  if choice == 'n' or choice == 'N':
    working = True
  else:
    working = False
