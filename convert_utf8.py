import datetime as dt
import sys
import os

for arg in sys.argv:
    print (arg)

n = arg
print("n is"+n)
n.split(".")
head, tail = os.path.split(n)
print(tail)
tail = tail.split(".")

filename = tail[0]
inputname = filename+".lrc"
outputname = filename+".ksc"
o= open(outputname,"w+")
o.write("karaoke := CreateKaraokeObject;\n")
o.write("karaoke.rows := 2;\n")
o.write("karaoke.clear;\n")
o.write("karaoke.font('Times New Roman');\n\n")
f = open(inputname, "rb")

def convertLine():
    global line
    line = line.decode().replace('[', ']')
    line = line.replace('\n', ']')
    x = line.split(']')
    x.pop(0)
    x.pop(-1)
    x.pop(-1)
    n = len(x)
    name = ""
    for i in range(1, n - 1, 2):
        name = name + x[i]
    time = ""
    for i in range(2, n + 1, 2):
        start = x[i - 2]
        end = x[i]
        start_dt = dt.datetime.strptime(start, '%M:%S.%f')
        end_dt = dt.datetime.strptime(end, '%M:%S.%f')
        diff = (end_dt - start_dt)
        a = diff.seconds * 1000 + diff.microseconds / 1000
        a = a.__int__()
        time = time + ',' + a.__str__()
    time = time[1:]
    o.write("karaoke.add(\'" + x[0] + "\', \'" + x[-1] + "\', \'" + name + "\', \'" + time + "\');\n")

line = f.readline()

while line:

    while len(line)<=20:
        line = f.readline()

    convertLine()
    line = f.readline()

f.close()
o.close()
