import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="change interface")
    parser.add_option("-m", "--mac", dest = "mac", help="change mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("tipe interface belum dimasukkan")
    elif not options.mac:
        parser.error("nomor mac belum dimasukkan")
    return options


def change_mac(interface, mac):
    # print("alamt mac dari " + interface + " sudah diganti dengan " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_addreas_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result));
    if mac_addreas_search_result:
        return mac_addreas_search_result.group()
    else:
        print("mac addreas tidak ditemukan");

# 00:15:5d:dc:0d:59
options = get_arguments();
interface = options.interface
mac = options.mac

current_mac = get_current_mac(interface)
# print("current mac saat ini adalah " + current_mac)

change_mac(interface, mac)
current_mac = get_current_mac(interface)
if current_mac == mac:
    print("mac addreas sudah terganti dengan " + current_mac)
else:
    print("tidak ada yang berubah")

    
