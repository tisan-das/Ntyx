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

from node import Node

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return items==[]

	def push(self,line_no,loopType):
		node = Node(line_no,loopType)
		self.items.append(node)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[len(self.items)-1]