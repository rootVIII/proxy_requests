## Python Proxy Requests | make an http GET/POST with a proxy scraped from https://www.sslproxies.org/
pypi.org: https://pypi.org/project/proxy-requests/
<br><br>
The ProxyRequests class first scrapes proxies from the web. Then it recursively attempts to make a request if the initial request with a proxy is unsuccessful. System Requirements: Python 3 and the requests module.
<br> Youtube Demo:  https://youtu.be/isxJeqo_sBA
<br><br>
Runs on Linux and Windows (and Mac probably)-<b>It may take a moment to run depending on current proxy.</b>
<br><br>
Either copy the code and put where you want it, or download via pip:
<br><br>
<code>
pip3 install proxy-requests
</code>
<br>
<code>
from proxy_requests.proxy_requests import ProxyRequests
</code>
<br><br>
or if you need the Basic Auth subclass as well:
<br>
<code>
from proxy_requests.proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
</code>
<br><br>
If the above import statement is used, method calls will be identical to the ones shown below. Pass a fully qualified URL when initializing an instance.
<br><br>
The ProxyRequestBasicAuth subclass has get(), get_with_headers(), post(), post_with_headers(), and post_file() methods that will override the Parent methods.
<br><br>

<b>example GET:</b><br>
<code>
  r = ProxyRequests("https://api.ipify.org")
</code>
<br>
<code>
  r.get()
</code>
<br>
<b>example GET with headers:</b><br>
<code>
h = {"User-Agent": "NCSA Mosaic/3.0 (Windows 95)"}
</code>
<br>
<code>
r = ProxyRequests("url here")
</code>
<br>
<code>
r.set_headers(h)
</code>
<br>
<code>
r.get_with_headers()
</code>
<br>
<b>example POST:</b><br>
<code>
  r = ProxyRequests("url here")
</code>
<br>
<code>
  r.post({"key1": "value1", "key2": "value2"})
</code>
<br>
<b>example POST with headers:</b>
<br>
<code>
  r = ProxyRequests("url here")
</code>
<br>
<code>
  r.set_headers({"name": "rootVIII", "secret_message": "7Yufs9KIfj33d"})
</code>
<br>
<code>
  r.post_with_headers({"key1": "value1", "key2": "value2"})
</code>
<br>
<b>example POST FILE:</b><br>
<code>
  r = ProxyRequests("url here")
</code>
<br>
<code>
  r.set_file({'file': open('test.txt', 'rb')})
</code>
<br>
<code>
  r.post_file()
</code>
<br>
<b>example GET with Basic Authentication:</b><br>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
</code>
<br>
<code>
  r.get()
</code>
<br>
<b>example GET with headers & Basic Authentication:</b><br>
<code>
h = {"User-Agent": "NCSA Mosaic/3.0 (Windows 95)"}
</code>
<br>
<code>
r = ProxyRequestsBasicAuth("url here", "username", "password")
</code>
<br>
<code>
r.set_headers(h)
</code>
<br>
<code>
r.get_with_headers()
</code>
<br>
<b>example POST with Basic Authentication</b><br>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
</code>
<br>
<code>
  r.post({"key1": "value1", "key2": "value2"})
</code>
<br>
<b>example POSTwith headers & Basic Authentication</b><br>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
</code>
<br>
<code>
  r.set_headers({"header_key": "header_value"})
</code>
<br>
<code>
  r.post_with_headers({"key1": "value1", "key2": "value2"})
</code>
<br>
<b>example POST FILE with Basic Authentication:</b><br>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
</code>
<br>
<code>
  r.set_file({'file': open('test.txt', 'rb')})
</code>
<br>
<code>
  r.post_file()
</code>
<br><br>
<strong>Response Methods:</strong>
<br><br>
  <b>Returns a string:</b>
<br>
<code>
  print(r)
</code>
<br>
<b>Get the response headers:</b>
<br>
<code>
  print(r.get_headers())
</code>
<br>
<b>Get the status code:</b>
<br>
<code>
  print(r.get_status_code())
</code>
<br>
<b>Get the proxy that was used to make the request:</b>
<br>
<code>
  print(r.get_proxy_used())
</code>
<br>
</code>
<br>
<b>To write response a to a file (including an image):</b>
<br>
<code>
  r.response_to_file()
</code>
<br>
<b>Or if you want to write raw content yourself: </b>
<br>
<code>
  r.get_raw()
</code>
<br>
<b>Load your response to JSON: </b>
<br>
<code>
  import json
</code>
<br>
<code>
  r = ProxyRequests(url)
</code>
<br>
<code>
  r.get()
</code>
<br>
<code>
  json.loads(r.get_raw().decode())
</code>
<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2018</b><br><br>
<br>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/ex1.png" alt="example1" height="675" width="950"><hr>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/ex2.png" alt="example1" height="675" width="950"><hr>

