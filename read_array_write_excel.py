#================================================================
# Code for an reading an array from PLC and moving it into Excel
#================================================================

from eip import PLC
comm = PLC()
comm.IPAddress = '100.100.100.100'
' xArray is the PLC tag being read and 5 is the number of arrays to read 
array = comm.Read('xArray[0]',5)

print (array)
[1234, 2345, 3456, 4567, 5678]
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
for i, value in enumerate(array):
	ws.cell(column=1,row=i+1,value=value)

<Cell 'Sheet'.A1>
<Cell 'Sheet'.A2>
<Cell 'Sheet'.A3>
<Cell 'Sheet'.A4>
<Cell 'Sheet'.A5>
wb.save('PLC_Read.xlsx')
