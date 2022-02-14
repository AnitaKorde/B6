import requests

resp = requests.get("http://127.0.0.1:8000/home_cbv/")
print(resp.content)

#resp = requests.post("http://127.0.0.1:8000/home_cbv/", data= {"key":"value"})
#print(resp)

#resp = requests.delete("http://127.0.0.1:8000/home_cbv/")
#print(resp.content)