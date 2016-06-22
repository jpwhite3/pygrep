from __future__ import print_function
import pygrep
import glob
import argparse

def main():
	parser = argparse.ArgumentParser(description='This is a pure Python based clone of the GREP command')
	parser.add_argument('expression', action="store", type=str, help="Regular expression to match against")
	parser.add_argument('filepath', action="store", type=str, help="Path to file to search in. supports wildcard globs")
	parser.add_argument('-i', action="store_true", default=False, dest="ignorecase", help="Ignore case")
	parser.add_argument('-v', action="store_true", default=False, dest="invert", help="Show lines that don't match")
	args = parser.parse_args()
	
	file_list = glob.glob(args.filepath)
	for f in file_list:
		if len(file_list) > 1:
			pygrep.eprint("\nResults for file: %s" % f)
			pygrep.eprint("-"*(len(f)+18))
		results = pygrep.grep(args.expression, f, ignorecase=args.ignorecase, invert=args.invert)
		for result in results:
			print(result)