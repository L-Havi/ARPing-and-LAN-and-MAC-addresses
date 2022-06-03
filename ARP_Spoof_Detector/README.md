This python script allows you to monitor your network interface and alerts you if it detects ARP spoofing attempts

It uses broadcast MAC address in local area network to create ARP request to detect any changes in current interface's ARP table. If changes are found it notifies user

This script works in any UNIX based operating systems and in Windows if Python is installed

## Usage

```
Syntax: python arp_spooff.py [--help] [--interface INTERFACE]

[*] Options:
  -i INTERFACE, --interface INTERFACE                             Specify interface that is monitored


[*] Example:
  python arpspoof_detector.py -i eth0                             Monitors network interface eth0 for ARP spoofing attempts

```

