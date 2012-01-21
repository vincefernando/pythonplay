#!/usr/bin/env python
# encoding: utf-8
"""
swap_columns.py

Created by Vince Fernando on 2012-01-21.
"""

# CONSTANTS are in capital letters
INPUT_FILE = '/Users/vincefernando/PYTHON/image.txt'
OUTPUT_FILE = '/Users/vincefernando/PYTHON/image_modified.txt'

import csv 

# Open file safely
with open(INPUT_FILE, 'r') as f:
    # Read entire file 
    # We go through the file and save to 'line' IF the line is
    # not empty. 
    # Perhaps not safe for large files
    lines = [line for line in f.readlines() if line.strip()]

# Initialise empty region list
regions = []

# Loop to find 'regions' (first field in line)
for line in lines:
    # Find first parameter in line and call it the region
    # Split the line on commas, and select 0 index in resulting
    # list. 
    region = line.split(',')[0]
    # Check to see if the region exists, if not add to region list
    if region not in regions:
        regions.append(region)
        
# Initialise the csv output writer and get the output_writer object
output_writer = csv.writer(open(OUTPUT_FILE, 'wb'), delimiter=',', quoting=csv.QUOTE_MINIMAL)


for line in lines:
    # Remove whitespace from line (especially '\n')
    # Return a list (items) which is split upon finding commas
    items = line.strip().split(',')
    
    # Take the first item of items (the region)
    # Return the index of the region from the regions list
    # Turn the index into a string
    # Assign the index as the replacement of the region.
    items[0] = str(regions.index(items[0]))

    # Write the row to the file
    output_writer.writerow(items)


# Lists
# [, ]

# Tuples
# (, )

# Dictionaries
# { key: value, }


    


