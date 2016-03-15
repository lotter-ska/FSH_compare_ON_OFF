# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 07:22:51 2016

@author: lkock

FSH Data Processing
"""
from Tkinter import Tk
from tkFileDialog import askopenfilename




def convert(dut,antennaF,lna):
#    dut="/FSH Data/20160309_GEO_Equipment/asuslaptop.csv"
    data= np.genfromtxt(dut,delimiter=',',dtype=None)
    freq=(data[45:-1,0]).astype(np.float)
    dbm=(data[45:-1,1]).astype(np.float)
    dbuV=dbm+107
    
#    antennaF="/RFI Archive/Equipment_Database/Passive_Antennas/Antenna_MESA_KLPDA1.csv"
    af=np.genfromtxt(antennaF,delimiter=',',dtype=None)
    f=(af[2:-1,0]).astype(np.float)
    af1=(af[2:-1,3]).astype(np.float)
    af2=interp(freq,f,af1)
#    calc e field
    g=np.genfromtxt(lna,delimiter=',',dtype=None)
    ff=(g[3:-1,0]).astype(np.float)   
    gg=(g[3:-1,1]).astype(np.float)
    gg1=interp(freq,ff,gg)
    
    
    dbuV_m=dbuV+af2-gg1
#    figure()
#    plot(freq,af2)
    return freq, dbuV_m



def on_off(on,off,labels):
    f1, e1=convert(on,filename,filename_lna)
    f2, e2=convert(off,filename,filename_lna)
    figure()    
    plot(f1,e1,label="DUT On")
    plot(f2,e2,label="DUT Off")
    legend()
    grid()
    xlabel("frequency [Hz]")
    ylabel("E Field [dBuV/m]")
    title(labels)
    savefig(labels)


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title="Select Antenna Cal File") # show an "Open" dialog box and return the path to the selected file
filename_lna = askopenfilename(title="Select LNA Cal File")
filename_ON = askopenfilename(title="Select Culprit ON Data file")
filename_OFF = askopenfilename(title="Select Culprit OFF Data file")


#Enter the Plot title:
pltT="Enter title here....."

on_off(filename_ON,filename_OFF,pltT) 






