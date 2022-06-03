This python script allows you to change your MAC address. It works in any UNIX based operating systems.

## Usage

```
Syntax: python mac_changer.py [--help] [--interface INTERFACE] [--mac MAC]

[*] Options:
  -i INTERFACE, --interface INTERFACE                   Specify interface that is used
  -m MAC, --mac MAC                                     Specify the new MAC address used in the chosen interface


[*] Example:
  python mac_changer.py -i eth0 -m 00:11:22:33:44:55    Changes MAC address to 00:11:22:33:44:55 for interface eth0

```
