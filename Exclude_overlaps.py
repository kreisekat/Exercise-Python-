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


def parse_csv(csv_file):
    """takes file.csv and parses it into list of dictionaries. While doing so
    it converts dictionary["position"] into an integer and dictionary["statsval"] 
    into float. it returns this list of dicts with the name not_sorted """
    # open csv file, read  
    with open(csv_file) as input:
        reader = csv.DictReader(input)
        # list of dic with converted values for position and statsval
        not_sorted = []
        for dic in reader:
            #convert value (type strg) for the key "position" to integer
            dic["position"] = int(dic["position"])
            #convert value (type strg) for key "statval" to float
            dic["statsval"] = float(dic["statsval"])
            # adds converted dic to list
            not_sorted.append(dic)
        return not_sorted
    
        
def sort_by_statsval(csv_file):
    """uses parse_csv to parse a csv file, which changes type of position and statsval,
    into int and float respectively, while creating a list of dictionaries called
    not_sorted. Then this function sorts this list of dictionaries from low to high 
    statsval and returns sorted_list (list of dicts)"""
    sorted_list = sorted(parse_csv(csv_file), key = itemgetter("statsval"))
    return sorted_list



def in_intervals(csv_file, bp_interval=1):
    """in_intervals takes a csv_file, parses it into a list of dictionaries 
    which is then sorted into "sorted_list" by calling function sort_by_statsval
    (which itself calls parse_csv to get an unsorted list of dicts)
    A new list of dictionaries, filtered_list, is created, where only
    dictionaries are appended whose positions do not lie in an interval (bp_interval)
    around positions that are already in the list."""
    
    sorted_list = sort_by_statsval(csv_file)
    #new,filtered list
    filtered_list = []
    #appends first dictionary from sorted_list, because this has the 
    #lowest statsval = highest significance, because it is sorted by that
    filtered_list.append(sorted_list[0])

    # every position in following dictionaries in sorted_list is checked 
    # against the positions(or more correctly an interval around this position)
    # from the dictionaries in the filtered_list by calling in_list
    # if the position is not in the filtered_list yet, the respective dict is appended
    for dic in sorted_list:
        #if position in dic is not already in an interval around positions in filtered_list it is appended to filtered_list
        if not in_filtered_list(dic, filtered_list, bp_interval):
            filtered_list.append(dic)
            #print("list appended")
    return filtered_list

    
def in_filtered_list(dic, filtered_list, bp_interval):
    """returns True if position of the tested dic lies in any of the 
    intervals around positions from dictionaries in filtered_list and if this is
    the same chromosome"""
    
    result = False

    #dic["position"] is checked agains all dictionary["position"]+/- bp_interval
    for dictionary in filtered_list:
        mini = dictionary["position"] - bp_interval
        maxi = dictionary["position"] + bp_interval
        if dic["position"] >= mini and dic["position"] <= maxi and dic["chromosome"] == dictionary["chromosome"]:
            result = True
            break
            
    return result


def filtered_list_to_csv(filtered_list):
    keys = filtered_list[0].keys()
    with open("output.csv", "w") as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(filtered_list)
    return output


print(in_intervals("divchr_simple_values.csv", 2))


#def main(csv_input, bp_interval = 1):
#    filtered_list = in_intervals(csv_input, bp_interval)
#    print("csv was filtered")
#    filtered_list_to_csv(filtered_list)
#    print("output file was created")
#    
#    
# 

# eventual problems: what if statsvals are the same? - how does sorted handle that?


if __name__ == "__main__":
    main("divchr_short_test_data.csv")
