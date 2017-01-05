'''
	This file is part of Ntyx.

    Ntyx is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Ntyx is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Ntyx.  If not, see <http://www.gnu.org/licenses/>.
'''

from stack import Stack
from node import Node


stack = Stack()
elif_pos = []

def modLCSAJ(array2d):
	modArray = []
	for element in array2d:
		if element[0]<=element[1]:
			modArray.append(element)
	return modArray

def computeLCSAJ(array2d,elif_pos):
	print("elif_pos: ",elif_pos)
	start_node = [1]
	for item in array2d:
		if item[0] not in start_node:
			start_node.append(item[0])
	lcsaj = []
	for start in start_node:
		for tupl in array2d:
			if start<=tupl[0]: #modified
				flag = 0
				for eles in elif_pos:
					if start<eles and eles<tupl[0]:
						print(str(eles)+" is within "+str(start)+" and "+str(tupl[0]))
						flag = 1
				if flag==0:
					if tupl[2]==1:
						lcsaj.append([start,tupl[0],tupl[1]+1,tupl[2]])
					elif tupl[2]==2:
						lcsaj.append([start,tupl[0]-1,tupl[1]+1,tupl[2]])
					else:
						lcsaj.append([start,tupl[0],tupl[1],tupl[2]])
	return modLCSAJ(lcsaj)
	# return lcsaj

def isBraceExists(target,line_no):
	file = open(target,"r")
	current_line_no = 0
	while current_line_no<line_no:
		line = file.readline()
		current_line_no = current_line_no+1
	if '{' not in line:
		#while '{' not in line and ';' not in line:
		while '{' not in line and line.strip()[len(line.strip())-1]!=';':
			line = file.readline()
			current_line_no = current_line_no+1
	if '{' not in line:
		return False
	return True

def readCFile(file_name):
	file = open(file_name)
	line_no = 0
	jump = []
	for line in file:	
		#print(line)
		line_no = line_no+1
		# print("line number: ",line_no)
		# print(line)
		if '}' in line and '{' in line and line.index('}')<line.index('{'):
			if stack.peek().loopType==1:
				print("brace poped for line: ",line_no)
				jump.append([stack.peek().line_no,line_no,stack.pop().loopType])
			else:
				print("brace popped for line: ",line_no)
				jump.append([stack.peek().line_no,line_no+1,stack.peek().loopType])
				jump.append([line_no+1,stack.peek().line_no,stack.pop().loopType])
		if 'if' in line and 'else' in line:
			elif_pos.append(line_no)
		if 'if' in line in line:
			# print("if/else exists in ",line_no)
			if isBraceExists(file_name,line_no):
				# brace exists
				print("brace pushed for line: ",line_no)
				stack.push(line_no,1)
			else:
				jump.append([line_no,line_no+2,1])
		elif 'else' in line in line:
			# print("if/else exists in ",line_no)
			if isBraceExists(file_name,line_no):
				# brace exists
				print("brace pushed for line: ",line_no)
				stack.push(line_no,2)
			else:
				jump.append([line_no,line_no+2,2])
		elif 'for' in line or 'while' in line:
			if isBraceExists(file_name,line_no):
				print("brace pushed for line: ",line_no)
				stack.push(line_no,0)
			else:
				print("No brace for line: ",line_no)
				jump.append([line_no,line_no+1,0])
				jump.append([line_no+1,line_no,0])
		elif '}' in line and stack.size()!=0:
			if stack.peek().loopType==1:
				print("brace popped for line: ",line_no)
				jump.append([stack.peek().line_no,line_no,stack.peek().loopType])
				node = stack.pop()
				if stack.peek().loopType == 0:				 # modified
					jump.append([node.line_no,stack.peek().line_no,0]) # modified
			elif stack.peek().loopType==0:
				print("brace popped for line: ",line_no)
				jump.append([stack.peek().line_no,line_no+1,stack.peek().loopType])
				jump.append([line_no-1,stack.peek().line_no,stack.pop().loopType])
			else:
				print("brace popped for line: ",line_no)
				jump.append([stack.peek().line_no,line_no,stack.pop().loopType])
		elif '}':
			last_line = line_no
	print(jump)
	print(stack.size())
	lcsaj = computeLCSAJ(jump,elif_pos)
	print(lcsaj)
	print("last line: ",last_line)
	lcsaj.append([last_line,last_line,"exit"])
	print("No. of LCSAJs: ",len(lcsaj))
	print("LCSAJs: ",lcsaj)
	writeLCSAJ(lcsaj)
	return (jump,lcsaj)

def writeLCSAJ(lcsaj):
	file = open("totalLCSAJ","w")
	# file.write("LCSAJ:\n\n")
	for tupl in lcsaj:
		file.write(str(tupl[0])+"->"+str(tupl[1])+"->"+str(tupl[2])+"\n")
	file.close()