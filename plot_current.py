#import matplotlib.pyplot as plt
import serial
import sys
from datetime import date
import time

x=range(0, 10, 1)
y1=[0]*10
y2=[0]*10
y3=[0]*10
ser = serial.Serial(sys.argv[1],sys.argv[2])

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="S_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

while True:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  line = ser.readline()
#  line2=float(line.strip().decode('utf-8'))
#  line = [str(val) for val in line2.split(" ")]
  print(line)
