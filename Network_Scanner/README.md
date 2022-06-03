This python script allows you to scan IP address or range of IP addresses in local area network. 

Basically this script does ARP request manually, but it displays the results and doesn't update ARP table

It works in any UNIX based operating systems or in Windows if Python is installed

## Usage

```
Syntax: python network_scanner.py [--help] [--target TARGET IP]

[*] Options:
  -t TARGET IP, --target TARGET IP                Specify target IP address or range of IP addresses


[*] Example:
  One IP address:
  python -t 192.168.153.131                       Scans IP address 192.168.153.131 and displays it and its MAC address
  
  Range of IP addresses:
  python -t 192.168.153.0/24                      Scans IP range 192.168.153.0 - 192.168.153.255 using CIDR notation and  
                                                  displays all IP addresses and their MAC addresses in this range

```
