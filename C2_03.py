# Importing data from fixed-width data files

import struct
import string

datafile = 'ch02-fixed-width-1M.data'

# This is where we define how to understand line of data from the file
mask = '9s14s5s'

with open(datafile, 'rb') as f:
    for line in f:
        fields = struct.Struct(mask).unpack_from(line)
        print("Fields: ", [field.strip() for field in fields])
