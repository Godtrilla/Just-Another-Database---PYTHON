import sys
import random
import os
import csv
import pandas as pd
import Database

'''
 This class manages the CSV files
 with raad and write functions
    '''

# file which holds the original parks information
parksFile = 'Parks2.csv'
parkDB = 'ParksDatabase.data'

'''
Variables below keep track of record size
and the number of records for search purposes
		'''

num_records = 748
record_size = 168


'''
Dictionary declarations that hold key:value pairs 
with an positive integer being the value and 
the ID number of the corresponding record being the
key.  ReverseIDmap is the inverse of idMap.
		'''

idMap = {}
reverseIDmap = {}


'''
This function reads the corresponding CSV file
and formats into a new file named file.data
		'''
def formatter(file):
    temp = pd.read_csv(file)
    temp = temp.to_string()


    value = 0
    with open(parkDB, "w") as f:
        f.write(temp)
    with open(parkDB, "r") as f:
        lines = f.readlines()
    with open(parkDB, "w") as f:
        for line in lines:
            f.write(line[5:])
            f.write("\n")
            key = line[5:12].strip()
            idMap.update({key: value})
            reverseIDmap.update({value: key})
            value += 1

    #  print(len(line))
    #   f.writelines(lines[1:])
    with open(parkDB, "r") as f:
        lines = f.readlines()
    with open(parkDB, "w")as f:
        f.writelines(lines[2:])
    f.close()



'''
Binary search function using code identifier 
but was not yet integrated correctly
		'''

def binarySearch(f, name):
    global middle
    low = 0
    high = num_records - 1
    Found = False
    Success = False

    while not Found and high >= low:
        middle = (low + high) // 2
        # middle = low + (high-low) // 2
        record, Success = Database.displayRecord(f, middle)
        middleid = record.split()
        middleidnum = middleid[0]
        if middleidnum == name:
            Found = True
        if middleidnum < name:
            low = middle + 1
        if middleidnum > name:
            high = middle - 1

    if (Found == True):
        return record, middle  # the record number of the record
    else:
        return -1, middle

#UNFINISHED FUNCTION
def output():
    return 0











