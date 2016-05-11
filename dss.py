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

def create_reader(file_name):
	return csv.reader(open(file_name, "r"), delimiter="\t", quoting=csv.QUOTE_NONE)

def is_male(string):
	string = string.upper()
	if string == "M":
		return True
	elif string == "F":
		return False
	raise Exception("Specified gender incorrect. Needs to be either M or F.")

parents = []
parents_are_male = []
try:
	child = create_reader(sys.argv[1])
	child_is_male = is_male(sys.argv[2])
	
	for file_name, gender in zip(sys.argv[3::2], sys.argv[4::2]):
		parents.append(create_reader(file_name))
		parents_are_male.append(is_male(gender))
except IndexError as e:
	print("Arguments: <CHILD_FILE> <CHILD_GENDER:M/F> <PARENT_1_FILE> <PARENT_1_GENDER:M/F> [<PARENT_2_FILE> <PARENT_2_GENDER:M/F>]")
	exit()
except Exception as e:
	print(e)
	exit()

is_both_parents = len(parents)>1

for child_line, parent_lines in zip(child, zip(*parents)):
	if child_line[0][0] == "#" or child_line[3] == "--":
		continue
	
	child_letters = list(child_line[3])
	
	parents_are_found = []
	parent_skipped = False
	all_matched = False
	for parent_line, parent_is_male in zip(parent_lines, parents_are_male):
		parents_are_found.append(False)
		if parent_line[3] == "--":
			parent_skipped = True
			continue
		
		if parent_is_male:
			if child_is_male and child_line[1] == "X":
				parent_skipped = True
				continue
			if child_line[1] == "MT":
				parent_skipped = True
				continue
		
		matches = [letter in parent_line[3] for letter in child_letters]
		if all(matches):
			all_matched = True
		else:
			for i, match in enumerate(matches):
				if match:
					del child_letters[i]
					break
			else:
				parents_are_found[-1] = True
	
	child_is_found = is_both_parents and not parent_skipped and not all_matched and child_letters
	
	if any(parents_are_found) or child_is_found:
		if all(parents_are_found):
			child_is_found = True
		parent_letters = []
		for parent_line, parent_is_found in zip(parent_lines, parents_are_found):
			parent_letters.append(parent_line[3] + ("!" if not child_is_found and not parent_skipped and parent_is_found else ""))
		print("{}\t{}\t{}\t{}\t{}".format(
			child_line[0],
			child_line[1],
			child_line[2],
			child_line[3] + ("!" if child_is_found and is_both_parents else ""),
			"\t".join(parent_letters)))
