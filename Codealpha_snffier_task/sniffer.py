from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


# Function to analyze packets
def packet_analyzer(packet):

    print("\n" + "=" * 70)
    print("PACKET CAPTURED AT:", datetime.now())
    print("=" * 70)

    # Check IP Layer
    if packet.haslayer(IP):

        ip_layer = packet[IP]

        print("Source IP Address      :", ip_layer.src)
        print("Destination IP Address :", ip_layer.dst)
        print("TTL (Time To Live)     :", ip_layer.ttl)
        print("Packet Length          :", len(packet))

        # TCP Protocol
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]

            print("\nProtocol Type          : TCP")
            print("Source Port           :", tcp_layer.sport)
            print("Destination Port      :", tcp_layer.dport)
            print("Sequence Number       :", tcp_layer.seq)
            print("Acknowledgment Number :", tcp_layer.ack)

        # UDP Protocol
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]

            print("\nProtocol Type          : UDP")
            print("Source Port           :", udp_layer.sport)
            print("Destination Port      :", udp_layer.dport)

        # ICMP Protocol
        elif packet.haslayer(ICMP):
            icmp_layer = packet[ICMP]

            print("\nProtocol Type          : ICMP")
            print("Type                  :", icmp_layer.type)
            print("Code                  :", icmp_layer.code)

        else:
            print("\nProtocol Type          : OTHER")

        # Payload Data
        if packet.haslayer(Raw):
            print("\nPayload Data Found")
            try:
                payload = packet[Raw].load
                print("Payload               :", payload[:100])  
            except:
                print("Could not decode payload")

    else:
        print("Non-IP Packet Captured")

    print("=" * 70)


# Start sniffing
def start_sniffer():
    print("\nStarting Network Sniffer...")
    print("Capturing packets in real time")
    print("Press CTRL + C to stop\n")

    sniff(prn=packet_analyzer, store=False)


# Main
if __name__ == "__main__":
    start_sniffer()
   