#!/usr/bin/python3

import * from FileProc

class dnsmasq(FileProc):
	def _custom_init(self):
		pass

	def _custom_proc(self, line):
		if line[0] == "#" or line[0] == ";":
			return
		self.output("if(dnsDomainIs(host, \"%s\")) { return my_proxy; }" % line)


