stu_list=[]
import sys

args = sys.argv

f = open(sys.argv[1], 'r')

for line in f.readlines():
    print(line, end='')
    linesp = line.split()
    linesp[2] = [linesp[0], linesp[3], linesp[4]]
    stu_list.append(linesp[2])


f.close()