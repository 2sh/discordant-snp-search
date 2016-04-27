#!/usr/bin/env python3
#
#	Discordant SNP Search
#	Copyright (C) 2016 2sh <contact@2sh.me>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import sys
import csv

def is_male(string):
	string = string.upper()
	if string == "M":
		return True
	elif string == "F":
		return False
	raise Exception("Specified gender incorrect. Needs to be either M or F")

try:
	child_reader = csv.reader(open(sys.argv[1], "r"), delimiter="\t", quoting=csv.QUOTE_NONE)
	parent_reader = csv.reader(open(sys.argv[2], "r"), delimiter="\t", quoting=csv.QUOTE_NONE)
	
	child_is_male = is_male(sys.argv[3])
	parent_is_male = is_male(sys.argv[4])
except IndexError as e:
	print("Arguments: <CHILD_FILE> <PARENT_FILE> <CHILD_GENDER:M/F> <PARENT_GENDER:M/F>")
	exit()
except Exception as e:
	print(e)
	exit()

for c_line, p_line in zip(child_reader, parent_reader):
	if c_line[0][0] == "#":
		continue
	
	if c_line[3] == "--" or p_line[3] == "--":
		continue
	
	if parent_is_male:
		if child_is_male and c_line[1] == "X":
			continue
		if c_line[1] == "MT":
			continue
	
	for letter in c_line[3]:
		if letter in p_line[3]:
			break
	else:
		print("{}\t{}\t{}\t{}!{}".format(c_line[0], c_line[1], c_line[2], c_line[3], p_line[3]))
