#!/usr/bin/python
from __future__ import with_statement
from tempfile import mkstemp
from shutil import move
import mmap
import sys
import os
import fileinput
from os import fdopen, remove

if (len(sys.argv) < 5):
	print("Usage: ./replace_str.py <directory> <file_type> <src_str> <dst_str>")
	exit(0)

dir = sys.argv[1]
file_type = sys.argv[2]
src_str = sys.argv[3]
dst_str = sys.argv[4]


for file in os.listdir(dir):
	if file.endswith("."+ file_type):
		fh, abs_path = mkstemp()
		file_path = os.path.join(dir, file)
		with fdopen(fh, 'w') as new_file:
			with open(file_path) as old_file:
    				for line in old_file:
					new_file.write(line.replace(src_str, dst_str))
		#remove original file
		remove(file_path)
		#move new file
		move(abs_path, file_path)

