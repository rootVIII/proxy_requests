## make an http GET/POST with a proxy scraped from https://www.sslproxies.org/
<br><br>
The ProxyRequests class first scrapes proxies from the web
<br><br>
Then it recursively attempts to make a request if the initial request with a proxy is unsuccessful
<br><br>
Runs on Linux and Windows-<b>may take a moment to run depending on current proxy</b>
<br><br>
Pass it a fully qualified URL when inializing an instance
<br><br>
The ProxyRequestBasicAuth subclass has a GET and POST that will override the P$
<br><br>
<b>example GET:</b><br>
&emsp;&nbsp;r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example POST:</b>
&emsp;&nbsp;r = ProxyRequests("http://ptsv2.com/t/706cu-1533594868/post")<br>
&emsp;&nbsp;r.post({"key1": "value1", "key2": "value2"})<br><br>
<b>example GET with Basic Authentication:</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("https://postman-echo.com/basic-auth/", "postman", "password")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example post with Basic Authentication</b><br>
r = ProxyRequestsBasicAuth("url here", "username", "password", "postman", "password")<br>
r.post({"key1": "value1", "key2": "value2"})<br>
print('\n')<br>
print(r)<br>
print('\n')<br>
print(r.get_headers())<br>
print('\n')<br>
print(r.get_status_code())<br>
print('\n')
print(r.to_json())<br>
print('\n')<br>
print(r.get_proxy_used())
<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<br><br>
The Python 2 version may give warnings due to the older requests module. Therefore the Python 3 version is recommended.
Please remove the .py2 extension off of the file name if using the Python 2 version.
<hr>
<b>Author: James Loye Colley  04AUG2018</b>
