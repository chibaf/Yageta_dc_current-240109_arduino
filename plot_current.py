import matplotlib.pyplot as plt
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
fn="C_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

while True:
  try:
    ttime=time.time()-start
    if ttime<0.001:
      ttime=0.0
    st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
    ss=str(time.time()-int(time.time()))
    rttime=round(ttime,2)
    line = ser.readline()
    line2=line.strip().decode('utf-8')
    line3=[val for val in line2.split(" ")]
    f.write(st+ss[1:5]+","+str(rttime)+","+line3[0]+","+line3[1]+","+line3[2]+"\n")
    print(line3)
    y1.pop(-1)
    y1.insert(0,float(line3[0]))
    y2.pop(-1)
    y2.insert(0,float(line3[1]))
    y3.pop(-1)
    y3.insert(0,float(line3[2]))
    plt.clf()
    plt.ylim(-.5,1)
    lin1,=plt.plot(x,y1,label="L1")
    lin2,=plt.plot(x,y2,label="L2")
    lin3,=plt.plot(x,y3,label="L3")
    plt.legend(handles=[lin1,lin2,lin3])
    plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    ser.close()
    f.close()
    break
exit()