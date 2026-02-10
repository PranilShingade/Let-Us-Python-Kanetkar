#h) Create a dictionary which stores the following data: 
# Interface IP Address status 
# eth0 1.1.1.1 up 
# eth1 2.2.2.2 up 
# wlan0 3.3.3.3 down 
# wlan1 4.4.4.4 up 
# Write a program to perform the following operations: 
# Find the status of a given interface. 
# Find interface and IP of all interfaces which are up. 
# Find the total number of interfaces. 
# Add two new entries to the dictionary

interfaces = {
    'eth0': {'IP': '1.1.1.1', 'status': 'up'},
    'eth1': {'IP': '2.2.2.2', 'status': 'up'},
    'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
    'wlan1': {'IP': '4.4.4.4', 'status': 'up'}
}

# Find status of a given interface
def get_interface_status(interface):
    return interfaces[interface]['status']

# Find interface and IP of all interfaces which are up
def get_up_interfaces():
    return {iface: data['IP'] for iface, data in interfaces.items()
            if data['status'] == 'up'}

# Find total number of interfaces
def get_total_interfaces():
    return len(interfaces)

# Add a new interface
def add_interface(interface, ip, status):
    interfaces[interface] = {'IP': ip, 'status': status}

# Operations
print("Status of eth0:", get_interface_status('eth0'))
print("Up interfaces and IPs:", get_up_interfaces())
print("Total interfaces:", get_total_interfaces())

# Add TWO new entries
add_interface('eth2', '5.5.5.5', 'up')
add_interface('wlan2', '6.6.6.6', 'down')

print("Updated interfaces:", interfaces)

# Output:
# Status of eth0: up
# Up interfaces and IPs: {'eth0': '1.1.1.1', 'eth1': '2.2.2.2', 'wlan1': '4.4.4.4'}
# Total interfaces: 4
# Updated interfaces: {
#  'eth0': {'IP': '1.1.1.1', 'status': 'up'},
#  'eth1': {'IP': '2.2.2.2', 'status': 'up'},
#  'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
#  'wlan1': {'IP': '4.4.4.4', 'status': 'up'},
#  'eth2': {'IP': '5.5.5.5', 'status': 'up'},
#  'wlan2': {'IP': '6.6.6.6', 'status': 'down'}
# }

# Explanation:
# A dictionary stores interface names as keys and IP address and status as values.
# The status of a given interface is accessed using nested keys.
# Interfaces with status 'up' are filtered and their IP addresses are displayed.
# The total number of interfaces is obtained using len().
# Two new interfaces are added by inserting new key–value pairs into the dictionary.
