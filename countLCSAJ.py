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

import os
import sys
from stack import Stack
import countHelper as ch
import countCovered as cc
import writeReport as wr
import changeDir as cd

target = input("Enter the program name: ")

cd.createDir("test")
cd.changeWorkingDir("test")
cd.copyFile(target,"test")
cd.copyFile("gdbFile.gdb","test")
cd.copyFile("input","test")
print("Current working Directory: ",os.getcwd())

command = "gcc -g -Wall "+target+" -std=c99 >out"
print(command)
if os.system(command)>0:
	print("Error exists")
	sys.exit(1)
lcsaj = []
jump = []
(jump,lcsaj) = ch.readCFile(target)

# Covered LCSAJ
# inputFile = input("Enter the test input file: ")
# command = "mv "+inputFile+" input"
# os.system(command)
command = "gdb --batch --command=gdbFile.gdb --args ./a.out >output"
os.system(command)

lines = []
cc.extractLines("output",lines)
lines = cc.modArray(lines)
print("Lines Executed: ",lines)

boollcsaj = cc.totalCovered(jump,lcsaj,lines)
print("Jump: ",jump)
# print("Covered Jump: ",boolJump)
boollcsaj[len(boollcsaj)-1] = True
print("Covered LCSAJ: ",boollcsaj)

# Report
reportFile = "report"
wr.initializeReport(reportFile)
wr.writeLCSAJ(reportFile,lcsaj)
coveredLCSAJCount = wr.writeCoveredLCSAJ(reportFile,lcsaj,boollcsaj)
wr.percentCovered(reportFile,len(lcsaj),coveredLCSAJCount)