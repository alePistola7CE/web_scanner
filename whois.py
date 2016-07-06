import os

def get_whois(domain_name):
	print('[*]Getting owner information..' + "\t")
	command = "whois" + " " + domain_name
	process = os.popen(command)
	results = str(process.read())
	
	return results	
	

