# CodeAlpha_Python-Network-Packet-Sniffer
A Python-based network packet sniffer built with Scapy to capture and analyze live network traffic packets including IP addresses, protocols, ports, and payload data.

# Python Network Packet Sniffer

## Overview

This project is a basic network packet sniffer developed in Python using the Scapy library. It captures live network packets flowing through the system and analyzes important information such as source IP address, destination IP address, protocol type, ports, packet length, and payload data.

The main purpose of this project is to understand how network communication works, how data travels between devices, and how different protocols operate at the packet level.

This project was developed as part of a Cyber Security internship task to gain practical knowledge about network traffic analysis and packet inspection.

---

## Features

- Captures live network traffic packets
- Detects Source and Destination IP addresses
- Identifies protocols such as TCP, UDP, and ICMP
- Displays source and destination port numbers
- Shows packet size and packet details
- Reads raw payload data when available
- Real-time packet capturing and analysis
- Helps understand network communication flow

---

## Technologies Used

- Python 3
- Scapy Library
- Npcap (Windows Packet Capture Driver)
- Visual Studio Code

---

## Protocols Supported

### TCP (Transmission Control Protocol)

Used for reliable communication such as:

- Web browsing
- HTTPS connections
- File transfers
- Email communication

### UDP (User Datagram Protocol)

Used for fast communication such as:

- Video streaming
- Online gaming
- Voice calls

### ICMP (Internet Control Message Protocol)

Used for:

- Ping requests
- Network diagnostics
- Error reporting

---

## Installation

Install Python:

Download Python and install it on your system.

Install Scapy library:

```bash
python -m pip install scapy
```

Install Npcap on Windows:

Download and install Npcap for packet capturing support.

---

## How to Run

Run the Python file:

```bash
python sniffer.py
```

Generate network traffic by:

- Opening websites
- Running ping commands
- Streaming videos

Stop the program:

```bash
CTRL + C
```

---

## Example Output

Packet Captured

Source IP: 192.168.1.10

Destination IP: 142.250.190.78

Protocol: TCP

Source Port: 51234

Destination Port: 443

Payload: GET / HTTP/1.1

---

## Learning Outcomes

Through this project I learned:

- Basics of packet sniffing
- Network packet structure
- TCP/IP protocol behavior
- Real-time traffic monitoring
- Packet analysis using Python
- Practical cyber security fundamentals

---

## Future Improvements

Possible improvements for future development:

- Save captured packets in log files
- Build graphical user interface
- Export packets to PCAP files
- Add packet filtering options
- Create protocol statistics dashboard
- Detect suspicious traffic patterns

---

## Project Purpose

The purpose of this project is educational and learning-focused. It demonstrates how packet capturing works in network security and helps understand the fundamentals of network monitoring.

---

## Author

Developed by: Your Name

Cyber Security Internship Project
