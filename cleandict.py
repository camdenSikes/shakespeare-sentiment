"""Takes in a dictionary as a text file and turns it into a csv"""
import csv

infile = open("dictionary.txt", r)
outfile = open("dictionary.csv", w)
dictwriter = csv.writer(outfile, delimiter = "\t")

for line in infile.readlines:
    