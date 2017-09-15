"""Karina Ionkina, Ibnul Jahan
SoftDev1 pd7
HW03 -- StI/O: Divine your Destiny!
2017-09-15
"""
#'r' -- read mode: file is only being read.
#file object is created
file = open("occupations.csv", 'r')

#.read() extracts a string that contains all characters in the file
#print file.read()
"""
.readline(): read a file line by line
print file.readline() 

#.readlines() returns array with separate lines
print file.readlines()
"""

#initialize empty dictionary
d = {}

#file.readlines is an array with the lines of the documents
#we parse starting at index 1
for str in file.readlines()[1:len(file.readlines())-1]:
    line = str.split(',')
    #if there are commas in the job class
    if len(line) > 2:
        the_key = ",".join(line[:len(line)-1])
        d[the_key] = float(line[len(line) - 1])
    else:
        d[line[0]] = float(line[1])
print d




    

