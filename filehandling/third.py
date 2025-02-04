# Write a function in python to count the number of lines from a text file
# "abc.txt" which is starting with an alphabet "T".
# Example: If the file "abc.txt" contains the following lines:
# My name is Sunil kc.
# There is a playground.
# An aeroplane is in the sky.
# The sky is pink. (5)

with open ('/Users/suhritsatyal/Desktop/python_softwarica1/filehandling/abc.txt') as f:
    print(f.read(5))