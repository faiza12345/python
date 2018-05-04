a=[]
waitingtime=[]
turnaroundtime=[]
n=int(raw_input('Total number of processes: '))
start_time=0
total=0
finishtime=0

for i in xrange(n):
	a.append([])
	a[i].append(raw_input('enter process name: '))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))
	finishtime=finishtime+a[i][2]
	waitingtime.append([])
	waitingtime[i].append(int(start_time-a[i][1]))
	turnaroundtime.append([])
	turnaroundtime[i].append(int(finsihtime-a[i][1]))
 	start_time=start_time+a[i][2]

a.sort(key=lambda a:a[1])
print 'Process \t Arrival time \t Burst time \t waiting time \t turnaround time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',waitingtime[i][3],'\t\t',turnaroundtime[i]
