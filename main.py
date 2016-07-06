from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_text import *
from whois import *

ROOT_DIR = 'companies'
crea_cartella(ROOT_DIR)

def gather_info(name, url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(url)
	nmap = get_nmap('-F', ip_address)
	robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	create_report(name, url, domain_name, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
	project_dir = ROOT_DIR + '/' + name
	crea_cartella(project_dir)
	scrivi_file(project_dir + "/full_url.txt", full_url)
	scrivi_file(project_dir + "/domain_name.txt", domain_name)
	scrivi_file(project_dir + "/nmap.txt", nmap)
	scrivi_file(project_dir + "/robots_txt.txt", robots_txt)
	scrivi_file(project_dir + "/whois.txt", whois)
	
name = input("[?]Companie name -> ")
url = input("[?]url -> ")
gather_info(name, url)
print("[!]"+ name + " scan succesfully complete")


	
