#Simple script to write circuit static IP info down and save it into a .txt file 
#Place location name to be saved in file name for ease of access
location = int(input('What is the location number?: '))
#Empty list for circuit info to store
circuitinfo = []
#Gathering circuit info
print('Enter the useable IP(s): ')
ip = input()
circuitinfo.append(str(ip))
print('Enter the gateway: ')
gateway = input()
circuitinfo.append(str(gateway))
print('Enter the subnetmask: ')
subnetmask = input()
circuitinfo.append(str(subnetmask))
print('Enter the first DNS: ')
dns1= input()
circuitinfo.append(str(dns1))
print('Enter the second DNS: ')
dns2 = input()
circuitinfo.append(str(dns2))
#Save to same folder as script in format "locationnumber circuit info"
with open(str(location) + ' Circuit.txt','w') as file:
    file.write('\n'.join(circuitinfo))