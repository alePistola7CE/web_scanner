import os

def get_nmap(options, ip):
	print('[*]Nmap scanning..' + "\t")
	command = "nmap " + options + " " + ip
	process = os.popen(command)
	results = str(process.read())
	
	return results
	


