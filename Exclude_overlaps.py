#!/usr/bin/env python
"""
Copyright (C) 2017, Katrin Kreisel

Exclude_overlaps.py is free software: you can redistribute it and/or modify
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
import csv

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
takes CSV file listing " ", chromosome, position, count1, count2, statsval, sequence,
(sorted with highest significance (= lowest statsval) at the top) takes each position
and removes any following position (with lower significance; higher statsval)
that lies within +/- the bp_interval (default = 1) around this position.""")
parser.add_argument("-v", "--verbose", action="store_true", help="""A more elaborate
section has not been created yet.""")
args = parser.parse_args()



dict_list=[]
minval = 1.0

#opens the file.csv and makes each line into a dict, the keys of each value
#being the column names in the first line
with open("chr11_test_data.csv") as input:
    reader = csv.DictReader(input)
    for dic in reader:
        if float(dic["statsval"]) < minval:
            dict_list.append(dic)
            minval = float(dic["statsval"])
            print("was appended")

        
print(dict_list)


#with open("chr11_output.csv", "w") as output:
 #   writer = csv.writer(output, delimiter = ' ')
#for dic in csv_input:
#    print(dic)
        
#csv_output = csv.reader(open("chr11_output.csv"))


    
# csv file as described above, bp_intervall will create an
# interval around a position in which lower significance
# peaks are "removed"

def main(csv_input, bp_interval = 1):
    pass

#take in a csv file and get the user to specify bp_interval
#default = 1

# open csv file
# parse the csv file into dicts (key = chromosome)
# while(?) creating the dicts, filter as follows: if position
# lies within the interval ( position +/- bp_interval) of
# a previously added position
# or maybe create dicts first and then go through each dictonary

# output new csv file that only contains the filtered rows
# should have the same structure as the input


if __name__ == "__main__":
    main(csv_input)
