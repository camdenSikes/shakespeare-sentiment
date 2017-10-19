"""Takes in a dictionary as a text file and turns it into a csv"""
import csv

infile = open("dict.txt", r)
outfile = open("dict.csv", w)
dictwriter = csv.writer(outfile, delimiter = "\t")