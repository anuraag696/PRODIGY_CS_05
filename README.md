# PRODIGY_CS_05
Developed a packet sniffer tool that captures and analyzes network packets. Displays relevant information such as source and destination IP addresses, protocols, and payload data. Ensured the ethical use of the tool for educational purposes only.

## Disclaimer

I the author of this script is not responsible for any misuse or damage caused by the tool. Use it at your own risk.

## Ethical Considerations

- Ensure you have proper authorization before using this tool on a network.
- Respect privacy laws and regulations.
- Use the tool for educational purposes only and avoid intercepting sensitive information without explicit consent.

Certainly! Below is a detailed description for the packet sniffer code provided earlier, formatted in a README.md file:

## Packet Sniffer Tool

This Python script is a basic packet sniffer tool developed using the Scapy library. It captures network packets and extracts relevant information such as source and destination IP addresses, protocols, and payload data.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage

1. Install the required dependencies by running:
   ```
   pip install scapy
   ```

2. Run the packet sniffer script:
   ```
   python packet_sniffer.py
   ```

## Description

The packet sniffer tool listens for incoming network packets and analyzes them using Scapy. Here's how it works:

- The `packet_callback` function is defined as the callback function for the packet sniffer. It is called whenever a packet is captured.
- It checks if the packet has an IP layer using `IP in packet`.
- If an IP layer is present, it extracts the source and destination IP addresses and the protocol using `packet[IP].src`, `packet[IP].dst`, and `packet[IP].proto` respectively.
- It prints the source IP, destination IP, and protocol.
- It checks if the packet has a TCP layer using `TCP in packet`.
- If a TCP layer exists, it extracts the source and destination ports using `packet[TCP].sport` and `packet[TCP].dport`.
- It prints the source port and destination port.
- It checks if the packet has a Raw layer (payload data) using `Raw in packet`.
- If a Raw layer exists, it extracts and prints the payload data using `packet[Raw].load`.
- The `main()` function starts the packet sniffing process using `sniff()` from Scapy.

## Ethical Use

- This tool is intended for educational purposes and should only be used on networks and systems for which you have explicit permission to monitor and analyze traffic.
- Always respect privacy and security considerations and ensure that you comply with all relevant laws and regulations regarding network monitoring and packet sniffing.

```
