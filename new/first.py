import requests
url="http://nikhil.info.np"
name=requests.get(url)
print(name.text)
if name.status_code == 200:
	print("page successfully loaded")
else:
	print("page not found")	
	print("Status Code: %d"%name.status_code)

