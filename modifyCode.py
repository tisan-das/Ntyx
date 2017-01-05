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

def modifyCCode(fileIP,fileOP):
	fileInput = open(fileIP,'r')
	fileOutput = open(fileOP,'w')
	line_no = 0;
	# prevLine and currLine
	# if only } or { present
	#	merge with prevLine
	#	delete currLine
	prevLine = 1
	for line in fileInput:
		if line_no==1:
			prevLine = line
			continue
		# Complete remaining
	fileInput.close()
	fileOutput.close()