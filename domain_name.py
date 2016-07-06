#from tld import get_tld
from tld import *

def get_domain_name(url):
	print('[*]Getting domain_name..' + "\t")
	domain_name = get_tld(url)
	
	return domain_name
	


