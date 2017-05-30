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
from operator import itemgetter

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

# open csv file, read  
with open("chr11_test_data.csv") as input:
    reader = csv.DictReader(input)
    #convert statsval to float and position to int for sorting and comparison
    not_sorted = []
    for dic in reader:
        dic["position"] = int(dic["position"])
#        print(dic)
        dic["statsval"] = float(dic["statsval"])
#        print(dic)
        not_sorted.append(dic)
        
   
#sort dicts by statsval from lowest to highest
sorted_list = sorted(not_sorted, key = itemgetter("statsval"))
#print("sorted list")
#print(sorted_list)

# list of dicts- only append dicts if an entry of the same chromosome with position +/- bp interval doesn't exist already

filtered_list = []
# adds the first dict (with lowest statsval) to filter -> subsequently higher statsval dicts are checked against this

filtered_list.append(sorted_list[0])

print("sorted list")
print(filtered_list)




def main(csv_input, bp_interval = 1):
    pass
    
        



# add first dict from dict reader to new list dict_list

# now go through all other entries of dict reader

# call function same_chr to check whether next entry lies on the same chromosome as any previous entry
# if it returns false: add entry to dict_list
# if it returns true:
# call function in_interval to check whether the value of position lies within bp_interval around position
# if it returns false: add entry to dict_list
# if it returns true:
# call function check_statsval to check which statsval is lower -> throw error if statsval of entry is lower than ones from the list

# eventual problems: what if statsvals are the same? - how does sorted handle that?


if __name__ == "__main__":
    main(csv_input)
