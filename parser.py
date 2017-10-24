#/bin/pyhton
# # 0stamp 1lpeak 2rpeak 3lrms 4rrms 5GBZ 6ICV 7FTA 8GQD 9HWU 10DHO38 11NAA 12TBB 13NRK 14NSY 15JXN 16HBG 17NAU 
#1491091200.081 1.000 0.839 0.542 0.333 1.64e+01 1.97e+01 6.79e+00 1.38e+01 1.19e+01 3.02e+01 1.66e+01 1.74e+01 9.11e+00 2.03e+01 1.63e+01 1.97e+01 1.05e+01

import time,re,sys 
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt

print len(sys.argv)
print sys.argv[1]


with open(sys.argv[1]) as f:
  data=f.read().splitlines()

for i in range(1,len(data)):
  data[i] = re.split('\s+', data[i]) 
  for j in range (0,len(data[i])):
      data[i][j] = float(data[i][j])

stamp=[]
datetime=[]
time=[]
GBZ=[]
GQD=[]
DHO38=[]

#f1=open('X', 'w+')
for i in range (1,len(data)):
#   print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[i][0]))+" "+str(data[i][5])+" "+str(data[i][8])+" "+str(data[i][10])
   stamp.append(float(data[i][0]))
 #  datetime.append(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[i][0]))))
   GBZ.append(float(data[i][5]))
   GQD.append(float(data[i][8]))
   DHO38.append(float(data[i][10]))

dates=[dt.datetime.fromtimestamp(ts) for ts in stamp]

plt.figure(figsize=(19.2, 10.8), dpi=100)
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title(sys.argv[1])
plt.plot(dates,DHO38,label="DH038")
plt.plot(dates,GBZ,label="GBZ")
plt.plot(dates,GQD,label="GQD")
plt.grid()
ax.set_xlabel("Local Time Bojnice SK")
ax.set_ylabel("Intensity")
plt.legend(shadow=True, fancybox=True)
#plt.show()
plt.savefig("all_"+sys.argv[1][-10:-3]+"png",dpi=100)

#f1.close()

# gnuplot 
#set xdata time
#set timefmt "%H:%M:%S"
#plot 'X' using 2:3 ps 0.3, 'X' using 2:4 ps 0.3, 'X' using 2:5 ps 0.3
#set xrange ["02:30:00":"23:59:59"]
#set format x "%H:%M:%S"
