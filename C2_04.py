# Importing data from tab-delimited files

import csv

filename = 'ch02-data.tab'

data = []
try:
    with open(filename) as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    print("Error reading CSV file at line {:s}: {:s}".format(reader.line_num, e))
    sys.exit(-1)

if header:
    print(header)
    print('===============================')

for datarow in data:
    print(datarow)
