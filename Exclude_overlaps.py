#!/usr/bin/env python
"""
Exclude_overlaps.py takes CSV file listing ,chromosome,position,
count1,count2,statsval,sequence, (sorted with highest significance (statsval)
at the top) takes each position and removes any following position
that lies within +/- the bp_interval around this position.

Copyright (C) 2017, Katrin Kreisel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import sys
try:
    import argparse
except ImportError:
	sys.stderr.write("[Error] The python module 'argparse' is not installed\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running 'sudo easy_install argparse'\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency 'argparser'")

parser = argparse.ArgumentParser(prog=sys.argv[0], description="""Exclude_overlaps.py
takes CSV file listing ,chromosome,position,
count1,count2,statsval,sequence, (sorted with highest significance (statsval)
at the top) takes each position and removes any following position (with lower significance)
that lies within +/- the bp_interval around this position.""")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

# csv file as described above, bp_intervall will create an
# interval around a position in which lower significance
# peaks are "removed"
def main(csvfile, bp_interval = 1):
    pass

#take in a csv file and get the user to specify bp_interval
#default = 1

# parse the csv file into dicts (key = chromosome)
# while(?) creating the dicts, filter as follows: if position
# lies within the interval ( position +/- bp_interval) of
# a previously added position

# output new csv file that only contains the filtered rows
# should have the same structure as the input




if __name__ == "__main__":
    main()
