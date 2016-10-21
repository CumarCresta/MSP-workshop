import requests
url=requests.get("http://google.com")
print(url)
if url.status_code == 200:
	print("page successfully loaded")
else:
	print("page not found")	
