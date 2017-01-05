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

def initializeReport(fileName):
	file = open(fileName,"w")
	file.write("-LCSAJ Report-\n")
	file.write("--------------\n\n")
	file.close()

def writeLCSAJ(fileName,array2d):
	file = open(fileName,"a")
	file.write("All possible LCSAJs: "+str(len(array2d))+"\n")
	for tupl in array2d:
		string = str(tupl[0])+" \t\t"+str(tupl[1])+" \t\t"+str(tupl[2])+"\n"
		file.write(string)
	file.write("\n\n")
	file.close()

def writeCoveredLCSAJ(fileName,lcsajArr,boollcsajArr):
	file = open(fileName,"a")
	length = 0
	for i in range(0,len(boollcsajArr)):
		if boollcsajArr[i]:
			length += 1
	file.write("Covered LCSAJs: "+str(length)+"\n")
	for i in range(0,len(lcsajArr)):
		tupl = lcsajArr[i]
		if boollcsajArr[i]:
			string = str(tupl[0])+" \t\t"+str(tupl[1])+" \t\t"+str(tupl[2])+"\n"
			file.write(string)
	file.write("\n\n")
	file.close()
	return length

def percentCovered(fileName,total,covered):
	file = open(fileName,"a")
	percent = covered*100/total
	string = "Precentage LCSAJ Covered: "+str(percent)+"%\n"
	file.write(string)
	file.write("\n\n")
	file.close()

def removeIntermediate():
	pass