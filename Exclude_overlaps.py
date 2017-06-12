#!/usr/bin/env python3

"""
Copyright (C) 2017, Katrin Kreisel

Exclude_overlaps.py is free software: you can redistribute it 
and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import sys
import csv
from operator import itemgetter


def parse_csv(csv_file):
    """parse_csv takes file.csv and parses it into list of dictionaries.  While 
    doing so it converts dictionary["position"] into an integer and dictionary["statsval"] 
    into float.  It returns this list of dicts with the name not_sorted """
    # Open csv file, read  
    with open(csv_file) as input:
        reader = csv.DictReader(input)
        # List of dic with converted values for position and statsval
        not_sorted = []
        for dic in reader:
            # Convert value (type strg) for the key "position" to integer
            dic["position"] = int(dic["position"])
            # Convert value (type strg) for key "statval" to float
            dic["statsval"] = float(dic["statsval"])
            # Adds converted dic to list
            not_sorted.append(dic)
        return not_sorted
 
    
def sort_by_statsval(csv_file):
    """sort_by_statsval uses parse_csv to parse a csv file while creating a 
    list of dictionaries called not_sorted.  Then this function sorts this 
    list of dictionaries from low to high statsval and returns sorted_list 
    (list of dicts)."""
    sorted_list = sorted(parse_csv(csv_file), key = itemgetter("statsval"))
    return sorted_list


def in_intervals(csv_file, bp_interval=1):
    """in_intervals takes a csv_file, parses it into a list of dictionaries 
    which is then sorted into "sorted_list".  A new list of dictionaries 
    called filtered_list is created, where only dictionaries are appended 
    whose positions do not lie in an interval (bp_interval) around positions 
    that are already in the list."""  
    sorted_list = sort_by_statsval(csv_file)
    filtered_list = []
    # Appends first dictionary from sorted_list, because this has the lowest statsval
    filtered_list.append(sorted_list[0])
    # Every position in following dictionaries in sorted_list is checked 
    # against the interval around the positions from the dictionaries in the 
    # filtered_list by calling in_list.  If the position is not in the 
    # filtered_list yet (also in respect to the chromosome), the respective 
    # dict is appended.
    for dic in sorted_list:
        if not in_filtered_list(dic, filtered_list, bp_interval):
            filtered_list.append(dic)
    return filtered_list

 
def in_filtered_list(dic, filtered_list, bp_interval):
    """returns True if position of the tested dic lies in any of the 
    intervals around positions from dictionaries in filtered_list but only if 
    it is on the same chromosome"""
    result = False
    # dic["position"] is checked agains all dictionary["position"]+/- bp_interval and the chromosome.
    for dictionary in filtered_list:
        mini = dictionary["position"] - bp_interval
        maxi = dictionary["position"] + bp_interval
        if dic["position"] >= mini and dic["position"] <= maxi and dic["chromosome"] == dictionary["chromosome"]:
            result = True
            break       
    return result


def filtered_list_to_csv(filtered_list, output_name):
    """Takes list of dictionaries (filtered_list) and creates an output csv file,
    where the first line is the keys of one dictionary and all dictionary values
    are written underneath it line by line."""
    # Makes keys of first dictionary the "column names" in the csv output file.
    keys = filtered_list[0].keys()
    with open(output_name, "w") as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(filtered_list)
    return output


def main():
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
                                     takes a csv file with these columns-,chromosome,position,count1,count2,statsval,sequence.   
                                     It gives out a filtered csv (name has to be specified by the user), where lower-significance 
                                     positions on the same chromosome are removed if they lie within a bp_interval (to be specified 
                                     by the user, default = 1) around a position of higher significance.""")
    parser.add_argument("-v", "--verbose", action="store_true", help="""Exclude_overlaps.py 
                        takes a csv file with these columns: '',chromosome,position,count1,
                        count2,statsval,sequence.  It parses this file into a list of dictionaries, 
                        each line being one dictionary, the keys being the column names (first 
                        line), and the values from the line being the corresponding value.   
                        Statsval is converted to float and position is converted to integer.  
                        A new list of dictionaries is created, filtering out positions of 
                        lower significance (higher statsval) that lie withing an interval 
                        (bp_interval) around positions of higher significance.  The user should 
                        make sure to specify the name or of the input file (.csv), the 
                        bp_interval as a whole number (will be converted to integer, by default 1) 
                        and the name of the desired output file .csv.""")
    parser.add_argument("-bp", "--bp_interval", default = 1, type = int, help ="""Please specify a bp_interval, default = 1. 
                        Less significant peaks will be filtered out from positions of more significant peaks +/- this interval, 
                        if they are on the same chromosome.""")
    parser.add_argument("-i", "--input", required = True, help = "Please specify what your input file is called.")
    parser.add_argument("-o", "--output", required = True, help = "Please specify what your outputfile is supposed to be called.")
    
    try:
        args = parser.parse_args()
        if not (args.input or args.output):
            parser.error("Please specify the input csv file and or the desired output csv file name.")
        elif type(args.bp_interval) != int:
            parser.error("Please make sure you enter a number for bp_interval")
        else:
            filtered_list = in_intervals(args.input, args.bp_interval)
            print("csv was filtered")
            filtered_list_to_csv(filtered_list, args.output)
            print("Output file was created")
    except IOError as e:
        parser.error(str(e))

if __name__ == "__main__":
    main()
