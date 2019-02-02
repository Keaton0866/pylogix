#================================================================
# Code for an reading an array from PLC and moving it into Excel
#================================================================

from eip import PLC
comm = PLC()
comm.IPAddress = '100.100.100.100'
' xArray is the PLC tag being read and 5 is the number of arrays to read 
array = comm.Read('xArray[0]',5)

import openpyxl
wb = openpyxl.load_workbook('Example.xlsx')
sheet1 = wb.get_sheet_by_name('Sheet1')


' Move all the values from the array into column 1 of the spreadsheet
for i, value in enumerate(array):
	sheet1.cell(column = 1, row = i+1, value = value)

' Save the workbook	
wb.save('Example_Read.xlsx')

# Other options for the array 
'''
' The following puts the entire list into a single cell
sheet1['A2'] = str(array)
sheet1['A2'].value
'[1234, 2345, 3456, 4567, 5678]'

' This takes a single item from the list into a single cell
sheet1['A2'] = str(array[1])
sheet1['A2'].value
'2345'
'''
