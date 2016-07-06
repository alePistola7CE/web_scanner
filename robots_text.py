import urllib.request
import io

def get_robots_txt(url):
	print('[*]Robots_txt scan..' + "\t")
	if url.endswith('/'):
		path = url
	else:
		path = url + "/"
	try:
		req = urllib.request.urlopen(path + 'robots.txt', data = None)
		data = io.TextIOWrapper(req, encoding='utf-8')
		
		return data.read()
	except urllib.error.HTTPError:
		print("Error!")
		
	

