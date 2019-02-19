A simple script for creating a TCP RST attack.

Using Python and Scapy, we build a TCP/IP packet with the 'RST' flag set to true.  
We then issue this packet to the target, posing as the victim, causing the TCP conversation to then end prematurely.

The script requires a target IP address, victim IP address, and target port
