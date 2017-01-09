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

def extractNumberFromLine(line):
	i = 0;
	number = 0
	# print(line)
	while i<len(line) and line[i]>='0' and line[i]<='9':
		number = number*10 + int(line[i])
		i += 1
	# print(number)
	return number

def extractLines(fileName,lines):
	file = open(fileName,"r")
	for line in file:
		num = extractNumberFromLine(line)
		if num>0:
			lines.append(num)
	return lines

def modArray(array):
	print("array length: ",len(array))
	mod = []
	i = 1
	while i<array[0]:
		mod.append(i)
		i += 1
	while len(array)>0:
		element = array.pop(0)
		if mod[len(mod)-1] == element-2:
			mod.append(element-1)
		mod.append(element)
	return mod

def totalCovered(jump,lcsaj,lines):
	boolLCSAJ = []
	for i in range(0,len(lcsaj)):
		boolLCSAJ.append(False)
		for k in range(0,len(lcsaj)):
			tupl = lcsaj[i]
			j = 0
			while j<len(lines)-2 and lines[j]!=tupl[0]:
				j += 1
			if j==len(lines):
				break
			while j<len(lines)-1 and lines[j]!=tupl[1]:
				j += 1
			if j==len(lines)-1:
				break
			if lines[j+1]!=tupl[2]:
				break
			boolLCSAJ[i] = True
	return boolLCSAJ

# def totalCovered(jump,lcsaj,lines):
# 	boolLCSAJ = []
# 	for i in range(0,len(lcsaj)):
# 		boolLCSAJ.append(False)
# 	for k in range(0,len(lcsaj)):
# 		items = lcsaj[k]
# 		for i in range(0,len(lines)-2):
# 			if lines[i]!=items[0]:
# 				continue
# 			j=i
# 			while j<len(lines)-1 and lines[j]!=items[1]:
# 				j += 1
# 			# if lines[j+1]==items[2]:
# 			while  j<len(lines) and lines[j]!=items[2]:
# 				j += 1
# 			if j!=len(lines):
# 				boolLCSAJ[k] = True		
# 	return boolLCSAJ

# def totalCovered(jump,lcsaj,lines):
# 	boolJump = []
# 	for item in jump:
# 		boolJump.append(False)
# 	boolLCSAJ = []
# 	for item in lcsaj:
# 		boolLCSAJ.append(False)
# 	for i in range(0,len(jump)):
# 		tupl = jump[i]
# 		for j in range(0,len(lines)-1):
# 			diff1 = tupl[0]-lines[j]
# 			diff2 = tupl[1]-lines[j+1]
# 			# if tupl[0]==lines[j] and tupl[1]==lines[j+1]:
# 			if diff1>=-1 and diff1<=1 and diff2>=-1 and diff2<=1:
# 				if (diff1>=0 and diff2>=0) or (diff1<=0 and diff2<=0):
# 					boolJump[i] = True
# 					break
# 	for i in range(0,len(lcsaj)):
# 		tupl = lcsaj[i]
# 		for j in range(0,len(jump)):
# 			jmptupl = jump[j]
# 			if tupl[1]==jmptupl[0] and tupl[2]==jmptupl[1] and boolJump[j]==True:
# 				boolLCSAJ[i] = True
# 				break
# 	return (boolJump,boolLCSAJ)

# def totalCovered(lcsaj,lines):
# 	boolArr = []
# 	for x in lines:
# 		boolArr.append(False)
# 	for tups in lcsaj:
# 		for i in range(0,len(lines)):
# 			j = i
# 			if lines[j] == tups[0]:
# 				while lines[j]+1==lines[j+1] and lines[j]!=tups[1]:
# 					j += 1
# 				if lines[j]==tups[1] and lines[j+1]==tups[2]:
# 					boolArr[i] = True
# 					break;
# 	return boolArr
