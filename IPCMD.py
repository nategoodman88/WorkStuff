#Allows use of Windows commands
import os 
#Ask IP that is troubleshooting
print('Enter the IP you want to ping and trace')
ip = input()
#Ping and traces IP
print('Pinging...')
os.system(f'ping {ip}')
print('\nPing complete. Tracing...')
os.system(f'tracert {ip}')
print('\nTrace complete. Done.')

