#!/usr/bin/env python
# Date: Dec 5, 2017

import psutil
import os
import curses
import curses.textpad
from curses.textpad import Textbox, rectangle

def cpu():
    for scpufreq in psutil.cpu_freq(percpu=True):
        s = scpufreq.current 
        print (int(s).__int__())
           #int(s).__int__())
#def cpux():
#   x = psutil.cpu_count()

#def cooling():

    
#def gpu():    
    
    
    
def mem():
    print (os.popen('free -m -t | grep Mem').readlines())


cpu()
mem()
#gpu()
#cooling()
#cpux()
