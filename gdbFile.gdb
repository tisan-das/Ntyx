#	This file is part of Ntyx.

#    Ntyx is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Ntyx is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Ntyx.  If not, see <http://www.gnu.org/licenses/>.


#  gdb --batch --command=test.gdb --args ./a.out

#set width 0
#set height 0
set verbose off
set logging off

break main

r <input

define traverse
	while(1)
		n
	end
end

traverse