#!/usr/bin/python3
# Base class for file processing. 
# Sub-class need to re-implement _custom_init().

class FileProc:
	_in_fd = None
	_out_fd = None
	_curr_ln = 0

	def __init__(self, in_file, out_file = sys.stdout):
		if in_file is sys.stdin:
			self._in_fd = sys.stdin
		else:
			self._in_fd = open(in_file, "r")

		if out_file is sys.stdout:
			self._out_fd = sys.stdout
		else:
			self._out_fd = open(out_file, "w")

		self._custom_init()
		self._proc()

	def __del__(self):
		if self._in_fd is sys.stdin:
			pass
		else:
			self._in_fd.close()

		if self._out_fd is sys.stdout:
			pass
		else:
			self._out_fd.close()

	def _custom_init():
		pass

	def _proc(self):
		self._curr_ln = 0
		line = self._in_fd.readline()
		while (line)
			self._curr_ln += 1
			self._custom_proc(line)
			line = self._in_fd.readline()

	def _custom_proc(self, line):
		pass

	def output(*argv):
		print(argv, file=self._out_fd)

