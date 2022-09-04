import http
import urllib3

url = "http://google.com"

http = urllib3.PoolManager()

r = http.request('GET', url)

print(r.data)

