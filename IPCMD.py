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
  print('\nPing complete. Tracing...')
  os.system(f'tracert {ip}')
  print('\nTrace complete. Trying to find dns host...')
  os.system(f'nslookup {ip}')
  print('\nDNS Trace complete.')
  print('\nPress n to troubleshoot another IP. Type anything else to quit.')
  choice = input()
  if choice == 'n' or choice == 'N':
    working = True
  else:
    working = False
