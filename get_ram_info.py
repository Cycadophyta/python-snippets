import os
import psutil

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(round(int(line.split()[2])/1024**2,2))

'''def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))
'''

print(psutil.cpu_percent())

print(getRAMinfo())
#print(getCPUuse())