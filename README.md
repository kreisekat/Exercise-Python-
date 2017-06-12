# Exercise-Python-

This repository is containing my first exercises in python and is ment as a practice platform using git.

Exclude_overlaps.py 
                        takes a csv file with these columns: '',chromosome,position,count1,
                        count2,statsval,sequence.  It parses this file into a list of dictionaries, 
                        each line being one dictionary, the keys being the column names (first 
                        line), and the values from the line being the corresponding value.   
                        Statsval is converted to float and position is converted to integer.  
                        A new list of dictionaries is created, filtering out positions of 
                        lower significance (higher statsval) that lie withing an interval 
                        (bp_interval) around positions of higher significance.  The user should 
                        make sure to specify the name or path of the input file (.csv), the 
                        bp_interval as a whole number (will be converted to integer, by default 1) 
                        and the name/path of the desired output file .csv.
