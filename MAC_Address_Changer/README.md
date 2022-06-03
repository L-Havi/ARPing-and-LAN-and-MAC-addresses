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

## Example

Changing MAC Address in Kali Linux VM (Works also outside virtual machine but virtual machine is used in this example)

Starting MAC address in eth0 is 00:0c:29:e3:c9:a9:

![start](https://user-images.githubusercontent.com/72817588/171943677-553b30db-726c-4598-9246-a098bfdcde72.jpg)

Executing with "python main.py -i eth0 -m 00:11:22:33:44:55"

![execute](https://user-images.githubusercontent.com/72817588/171944638-1a140414-6bd0-4ad9-b3b9-2b9b09c75efb.jpg)

Now MAC address for interface eth0 has been changed to 00:11:22:33:44:55

![result](https://user-images.githubusercontent.com/72817588/171945217-d0211ea9-5715-4ff1-8ba3-89a47d163b8d.jpg)
