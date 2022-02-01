# reading file

import sys

#####################################
print('opening files...')

f1 = open('mydoc1', 'r')
f2 = open('mydoc2', 'r')
bf1 = open('mydoc3', 'rb')
bf2 = open('mydoc4', 'rb')

#####################################
# reading data

def reading_data(f):
    while True:
        data = f.readline()
        if (data == '') or (data == None):
            break

        sys.stdout.write(data)