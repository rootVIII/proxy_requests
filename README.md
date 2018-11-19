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
<br>
or if you need the Basic Auth subclass as well:
<br><br>
<code>
from proxy_requests.proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
</code>
<br><br>
If the above import statement is used, method calls will be identical to the ones shown below. Pass a fully qualified URL when initializing an instance.
<br><br>
The ProxyRequestBasicAuth subclass has get, post, post_with_headers, and post_file methods that will override the Parent methods.
<br><br>

<b>example GET:</b>
<code>
  r = ProxyRequests("https://api.ipify.org")
  r.get()
</code>

<b>example POST:</b>
<code>
  r = ProxyRequests("url here")
  r.post({"key1": "value1", "key2": "value2"})
</code>

<b>example POST with headers:</b>
<code>
  r = ProxyRequests("url here")<br>
  r.set_headers({"name": "rootVIII", "secret_message": "7Yufs9KIfj33d"})
  r.post_with_headers({"key1": "value1", "key2": "value2"})
</code>

<b>example POST FILE:</b>
<code>
  r = ProxyRequests("url here")
  r.set_file({'file': open('test.txt', 'rb')})
  r.post_file()
</code>

<b>example GET with Basic Authentication:</b>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
  r.get()
</code>

<b>example post with Basic Authentication</b>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
  r.post({"key1": "value1", "key2": "value2"})
</code>

<b>example post with headers & Basic Authentication</b>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
  r.set_headers({"header_key": "header_value"})<br>
  r.post_with_headers({"key1": "value1", "key2": "value2"})
</code>

<b>example POST FILE with Basic Authentication:</b>
<code>
  r = ProxyRequestsBasicAuth("url here", "username", "password")
  r.set_file({'file': open('test.txt', 'rb')})
  r.post_file()
  print(r)<br>
  print(r.get_headers())<br>
  print(r.get_status_code())<br>
  print(r.to_json())<br>
  print(r.get_proxy_used())
</code>
<br>
The to_json() method is not intended to be used for a string of HTML
<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2018</b><br><br>
Example 1:<br>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/example.png" alt="example1" height="675" width="950"><hr>
Example 2:<br>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/example_post_with_headers.png" alt="example2" height="1100" width="950">
