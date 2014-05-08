import psutil
import sys
from optparse import OptionParser
import matplotlib.pyplot as plt
import time

parser = OptionParser()
parser.add_option("--cpumax", dest="cpumax",help="Limite superior de CPU")
parser.add_option("--cpumin", dest="cpumin",help="Limite inferior de CPU")
parser.add_option("--memmax", dest="memmax",help="Limite superior de memoria")
parser.add_option("--memmin", dest="memmin",help="Limite inferiro de memoria")

(options, args) = parser.parse_args()
lCpuMax = float(options.cpumax)
lCpuMin = float(options.cpumin)
lMemMax = float(options.memmax)
lMemMin = float(options.memmin)

'''
teste grafico
'''
y=[]
x=[]
maxcpu=[]
mincpu=[]
maxmem=[]
minmem=[]
netsent=[]
netrecv=[]

try:
	psutil.cpu_percent(interval=0)
	bytessend = psutil.network_io_counters().bytes_sent
	bytesrecv = psutil.network_io_counters().bytes_recv
	while True:

		leituraCPU =  psutil.cpu_percent(interval=0)
		leituraMem = psutil.phymem_usage().percent

#		print "Leitura CPU" , leituraCPU
#		print "Leitura Mem", leituraMem
#		print "lMemMax", lMemMax	
#		print "lMemMin", lMemMin	
		
		
		x.append(leituraCPU)
		y.append(leituraMem) 	
		maxcpu.append(lCpuMax)
		mincpu.append(lCpuMin)
		maxmem.append(lMemMax)
		minmem.append(lMemMin)


		#Controle dos limites

		if  lCpuMax < leituraCPU:
			print "CPU - Limite superior excedido"

		if lCpuMin > leituraCPU:
			print "CPU - Limite inferior excedido"

		#Leitura da Memoria		

		if lMemMax < leituraMem:
			print "MEM - Limite superior excedido"
		
		if lMemMin > leituraMem:
			print "MEM - Limite inferior excedido"



		print "Bytes Recieved (kbps) : ", (psutil.network_io_counters().bytes_recv - bytesrecv)/1024.
		print "Bytes Sent (kbps) : ", (psutil.network_io_counters().bytes_sent - bytessend)/1024.


		netsent.append((psutil.network_io_counters().bytes_sent - bytessend)/1024)
		netrecv.append((psutil.network_io_counters().bytes_recv - bytesrecv)/1024)

		bytessend = psutil.network_io_counters().bytes_sent
		bytesrecv = psutil.network_io_counters().bytes_recv

		time.sleep(1)	
 
except KeyboardInterrupt:
	

	#Graph 1 - CPU / Memory
	plt.figure(1)
	plt.subplot(211)
	plt.ylabel('Consumo CPU (%)')
	plt.xlabel('Tempo')
	plt.plot(x)
	plt.subplot(211)
	plt.plot(maxcpu)
	plt.subplot(211)
	plt.plot(mincpu)
	plt.subplot(212)
	plt.ylabel('Consumo RAM (%)')
	plt.xlabel('Tempo')
	plt.plot(y)
	plt.subplot(212)
	plt.plot(maxmem)
	plt.subplot(212)
	plt.plot(minmem)

	#Graf 2 - Net troghput
	plt.figure(2)
	plt.subplot(211)
	plt.ylabel("NET Sent KBPS")
	plt.plot(netsent)
	plt.subplot(212)
	plt.ylabel("NET Recieved KBPS")
	plt.plot(netrecv)
	plt.show()
	pass
    



	

