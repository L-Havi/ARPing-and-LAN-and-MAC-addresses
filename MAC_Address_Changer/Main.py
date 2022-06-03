#!/usr/bin/env python

import optparse
import subprocess
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify a valid interface, use --help for more info")
    elif not options.mac_address:
        parser.error("[-] Please specify a valid MAC address, use --help for more info")
    else:
        return options


def change_mac(interface, mac_address):
    print("[+] Changing MAC address for " + interface)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


options = get_arguments()
mac = current_mac(options.interface)
print("[+] Current MAC address for " + options.interface + ": " + str(mac))

change_mac(options.interface, options.mac_address)

mac = current_mac(options.interface)
if mac == options.mac_address:
    print("[+] MAC address for " + options.interface + " was successfully changed to " + options.mac_address)
else:
    print("[-] MAC address did not get changed")
