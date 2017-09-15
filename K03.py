"""Karina Ionkina, Ibnul Jahan
SoftDev1 pd7
HW03 -- StI/O: Divine your Destiny!
2017-09-15
"""
#'r' -- read mode: file is only being read.
#file object is created
file = open("occupations.csv", 'r')

"""
#.read() extracts a string that contains all characters in the file
print file.read()

.readline(): read a file line by line
print file.readline() 

#.readlines() returns array with separate lines
print file.readlines()

"""

d = {}
for str in file.readlines():
    x = str.split(',')
    print x
    

    

