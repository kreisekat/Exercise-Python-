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
    """takes file.csv and parses it into list of dicts and converts position
    into int and statsval into float. list of dicts is called not_sorted """
    # open csv file, read  
    with open(csv_file) as input:
        reader = csv.DictReader(input)
        #convert statsval to float and position to int for sorting and comparison
        not_sorted = []
        for dic in reader:
            dic["position"] = int(dic["position"])
    #        print(dic)
            dic["statsval"] = float(dic["statsval"])
    #        print(dic)
            not_sorted.append(dic)
        return not_sorted
    
#print(parse_csv("divchr_short_test_data.csv"))
        
def sort_by_statsval(csv_file):
    """uses parse_csv to parse a csv file, and changes type of position and statsval,
    into int and float respectively, then sorts it from low to high statsval and 
    returns sorted_list (list of dicts)"""
    sorted_list = sorted(parse_csv(csv_file), key = itemgetter("statsval"))
    return sorted_list

#print(sort_by_statsval("divchr_short_test_data.csv"))
    


# list of dicts- only append dicts if an entry with position +/- bp interval doesn't exist already


# adds the first dict (with lowest statsval) to filter -> subsequently higher statsval dicts are checked against this


def in_interval(csv_file, bp_interval=1):
    sorted_list = sort_by_statsval(csv_file)
    new_list = []
    new_list.append(sorted_list[0])
    #print(new_list)

    
    for dic in sorted_list:
        print("in the outer for loop")
        
        for dictionary in new_list:
#            mini = dictionary["position"] - bp_interval
#            maxi = dictionary["position"] + bp_interval
            print("in the nested forloop")
            new_list.append(dic)
            break
#            if dic["position"] < mini and dic["position"] > maxi:
#                print("in the if statement of the nested for loop")
#                new_list.append(dic)
    return new_list
            
    
#    return new_list
            
#    """ compares all dicts of the sorted_list to the filtered list, if the dict
#    position doesn't lie in a bp interval around previously existing positions
#    add to filtered_list"""
#    sorted_list = sort_by_statsval(csv_file)
#    filtered_list = []
#    filtered_list.append(sorted_list[0])
#
#    for dic in sorted_list:
#        if not any(dic["position"] == d["position"] for d in filtered_list):
#            filtered_list.append(dic)
#            
#            if not dic["position"] in range((d["position"]-bp_interval), (d["position"]+bp_interval)) for d in filtered_list:
#                filtered_list.append(dic)
        
#comparison for just checking the position without interval
#        if not any(dic["position"] == d["position"] for d in filtered_list):
#            filtered_list.append(dic)
#        if any(dic["position"] < (d["position"]-bp_interval) for d in filtered_list):
#            filtered_list.append(dic)
#            
#        if any(dic["position"] > (d["position"]+bp_interval) for d in filtered_list):
#            filtered_list.append(dic)
            
        #else: do nothing 
        
#    return filtered_list

        
            



print("after in_interval")
print(in_interval("divchr_short_test_data.csv", 1))

def main(csv_input, bp_interval = 1):
    pass
    
        

#print("test for interval comparison in in_interval")
#val1 = 3.9
#val2 = 6
#bp_interval = 2
#
#if val1 >= (val2-bp_interval) and val1 <= (val2+bp_interval):
#    print("val1 in interval of val2")
#else:
#    print("val1 not in interval of val2")

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
    main("divchr_short_test_data.csv")
