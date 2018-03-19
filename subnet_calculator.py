import sys
import math

#Script to calculate IPv4 addressing scheme information

def calc_hosts(s):
	hosts = math.pow(2,int(s)) #2 to power of s will produce the number of IPv4 hosts per subnet. s is the number of bits to use for the host.
	hosts = hosts - 2 #subtract the broadcast and network ID
	return int(hosts)

def calc_networks(n):
	networks = math.pow(2, int(n))
	networks = int(networks)
	return int(networks)

def main():
	s = raw_input("How many host bits?")
	n = raw_input("How many network bits?")
	hosts = calc_hosts(s)
	networks = calc_networks(n)
	print("This will produce %s hosts per subnet with %s networks." % (hosts, networks))

if __name__ == '__main__':
	main()
	
	
