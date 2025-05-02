from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_callback(packet):
    print("\n" + "="*50)
    print(f"📅 Time: {datetime.now()}")

    # Check for IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"🌐 Source IP: {ip_layer.src}")
        print(f"🌐 Destination IP: {ip_layer.dst}")
        print(f"📦 Protocol: {ip_layer.proto}")

        # TCP or UDP layer
        if TCP in packet:
            print("🔗 TCP Segment")
            print(f"➡️ Source Port: {packet[TCP].sport}")
            print(f"⬅️ Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print("🔗 UDP Segment")
            print(f"➡️ Source Port: {packet[UDP].sport}")
            print(f"⬅️ Destination Port: {packet[UDP].dport}")

        # Payload
        if Raw in packet:
            payload = packet[Raw].load
            try:
                decoded = payload.decode(errors='ignore')
                print(f"📄 Payload: {decoded}")
            except Exception:
                print("📄 Payload: <unable to decode>")
    else:
        print("Packet does not contain an IP layer")

# Start sniffing (you can change 'count=0' to a number to limit captures)
print("🔍 Starting Packet Sniffer... Press CTRL+C to stop.")
sniff(prn=packet_callback, store=0)
