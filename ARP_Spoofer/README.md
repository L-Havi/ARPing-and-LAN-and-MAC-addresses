This python script allows you to execute MITM attack using ARP Spoofing. Only for demonstration purposes. All types of malicious usage strictly forbidden

It uses broadcast MAC address in local area network to create ARP request using target IP address and LAN router IP address. This causes both router and target machine to update their ARP tables associating users IP address with router's/target's MAC address and redirecting all data frames through your machine

This script works in any UNIX based operating systems and in Windows if Python is installed

## Usage

```
Syntax: python arp_spoof.py [--help] [--target TARGET IP] [--router ROUTER IP]

[*] Options:
  -t TARGET IP, --target TARGET IP                            Specify target IP Address that is used
  -r ROUTER IP, --router ROUTER IP                            Specify the router's IP Address


[*] Example:
  python arp_spoof.py -t 192.168.153.129 -r 192.168.153.1     Starts ARP spoofing between target IP 192.168.153.129 and router IP 192.168.153.1

```
