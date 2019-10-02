#!/usr/bin/python3

from FileProc import *

class dnsmasq(FileProc):
	def _custom_init(self):
		pass

	def _custom_proc(self, line):
		if len(line) == 0:
			# blank line
			return
		if line[0] == "#" or line[0] == ";":
			return
		self.output("if(dnsDomainIs(host, \"%s\")) { return my_proxy; }" % line)

if __name__ == "__main__":
	a = dnsmasq(sys.stdin)

