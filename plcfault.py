#!/usr/bin/python

from optparse import OptionParser
from eip import PLC

def parse_cli():

    ''' CLI parser using OptionParser'''


    parser = OptionParser()

    parser.add_option('-d', '--debug',

                      dest='debug',

                      default=False,

                      help='Enable debug output',

                      action='store_true')

    parser.add_option('-a', '--address',

                      dest='address',

                      default="10.202.1.2",

                      help='PLC IP Address',

                      type='string',

                      action='store')

    parser.add_option('-t', '--tag',

                      dest='tag',

                      default="pattest",

                      help='read a tag',

                      type='string',

                      action='store')
    
    parser.add_option('-f', '--fault',

                      dest='fault',

                      default="gCELL1_FAULT.DATA",

                      help='array of faults',

                      type='string',

                      action='store')
    
    parser.add_option('-l', '--list',

                      dest='list',

                      default="False",

                      help='List of IP devices',

                      action='store_true')


    return parser.parse_args()


(options, args) = parse_cli()

def ex_getPLCTime():
    '''
    get the PLC's clock time
    '''
    ret = comm.GetPLCTime()
    return ret

#initiate
comm = PLC()
comm.IPAddress = options.address

#get current plc time
time = ex_getPLCTime()
print ("Current PLC time is:",time)

#Ethernet IP devices
if options.list == True:
    '''
    discover all the Ethernet I/P devices on the network and print the
    results
    '''
    print ("Discovering Ethernet I/P devices, please wait...")
    device = comm.Discover()
    
    for i in range(len(device)):
        print ('(' + str(i+1) + ') ' + device[i].IPAddress)
        print ("     ProductName/Code - ", device[i].ProductName, "(" + str(device[i].ProductCode) + ")")
        print ("     Vendor/DeviceID  - ", device[i].Vendor, "(" + str(device[i].DeviceID) + ")")
        print ("     Revision/Serial  - ", device[i].Revision, device[i].SerialNumber)
        print ("")
    print ("Total number of devices found (in no particular order):", len(device))
    print ("")

print ("")

if options.fault == True:
    faults = comm.Read(options.fault,151)
    for i in range(0,len(faults)):
        if faults[i] != 0:
            fault2 = options.tag +  '[' + str(i) + ']'
        
            print (fault2)
            fault3 = comm.Read(fault2)
            #fault3 = bin(fault3)
            print (fault3)
        
            '''
            for j in range(0,32):
                if fault3[j] != 0:
                    fault4 = fault2 + '.' + str(j)
                    print("Error on",fault4)
            '''

tagvalue = comm.Read(options.tag)
print (options.tag,"is",tagvalue)



















