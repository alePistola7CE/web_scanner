import os


def crea_cartella(nome):
	if not os.path.exists(nome):
		os.makedirs(nome)

def scrivi_file(percorso, data):
	f = open(percorso, 'w')
	try:
		f.write(data)
		f.close()
	except TypeError:
		f.close()
	




