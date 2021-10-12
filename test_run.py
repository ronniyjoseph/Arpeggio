# -*- mode: python; coding: utf-8 -*
# Copyright (c) 2018 Radio Astronomy Software Group
# Licensed under the 3-clause BSD License

import argparse
import os
import time as pytime
from datetime import timedelta, datetime

import pyuvsim

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		#description="A command-line script to execute a pyuvsim simulation from a parameter file."
	)
	parser.add_argument('paramsfile', type=str, help='Parameter yaml file.', default=None)
	parser.add_argument('--profile', type=str, help='Time profiling output file name.')
	parser.add_argument('--quiet', action='store_true', help='Suppress stdout printing.')
	parser.add_argument('--raw_profile', help='Also save pickled LineStats data for line profiling.',
						action='store_true')

	args = parser.parse_args()

	print("Finishes Parsing")

	if not os.path.isdir(os.path.dirname(args.paramsfile)):
		args.paramsfile = os.path.join('.', args.paramsfile)

	t0 = pytime.time()

	pyuvsim.uvsim.run_uvsim(args.paramsfile, quiet=args.quiet)
