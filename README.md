## make an http GET/POST with a proxy scraped from https://www.sslproxies.org/
The ProxyRequests class first scrapes proxies from the web
<br><br>
Then it recursively attempts to make a request if the initial request with a proxy is unsuccessful
<br><br>
Requirements: Python 3 and the requests module
<br><br>
JUST ADDED TO PYPI...    pip install proxy-requests (or pip3 install proxy-requests)
<br><br>
Runs on Linux and Windows-<b>may take a moment to run depending on current proxy</b>
<br><br>
python3 -m pip install --index-url https://test.pypi.org/simple/ proxy_requests
<br><br>
Pass it a fully qualified URL when initializing an instance
<br><br>
The ProxyRequestBasicAuth subclass has get, post, post_with_headers, and post_file methods that will override the Parent methods
<br><br>
<b>example GET:</b><br>
&emsp;&nbsp;r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example POST:</b><br>
&emsp;&nbsp;r = ProxyRequests("url here")<br>
&emsp;&nbsp;r.post({"key1": "value1", "key2": "value2"})<br><br>
<b>example POST with headers:</b><br>
&emsp;&nbsp;r = ProxyRequests("url here")<br>
&emsp;&nbsp;r.set_headers({"name": "rootVIII", "secret_message": "7Yufs9KIfj33d"})<br>
&emsp;&nbsp;r.post_with_headers({"key1": "value1", "key2": "value2"})<br><br>
<b>example POST FILE:</b><br>
&emsp;&nbsp;r = ProxyRequests("url here")<br>
&emsp;&nbsp;r.set_file({'file': open('test.txt', 'rb')})<br>
&emsp;&nbsp;r.post_file()<br><br>
<b>example GET with Basic Authentication:</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("url here", "username", "password")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example post with Basic Authentication</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("url here", "username", "password")<br>
&emsp;&nbsp;r.post({"key1": "value1", "key2": "value2"})<br><br>
<b>example post with headers & Basic Authentication</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("url here", "username", "password")<br>
&emsp;&nbsp;r.set_headers({"header_key": "header_value"})<br>
&emsp;&nbsp;r.post_with_headers({"key1": "value1", "key2": "value2"})<br><br>
<b>example POST FILE with Basic Authentication:</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("url here", "username", "password")<br>
&emsp;&nbsp;r.set_file({'file': open('test.txt', 'rb')})<br>
&emsp;&nbsp;r.post_file()<br><br>
&emsp;&nbsp;print(r)<br>
&emsp;&nbsp;print(r.get_headers())<br>
&emsp;&nbsp;print(r.get_status_code())<br>
&emsp;&nbsp;print(r.to_json())<br>
&emsp;&nbsp;print(r.get_proxy_used())
<br><br>
The to_json() method is not intended to be used for a string of HTML<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2018</b><br><br>
Example 1:<br>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/example.png" alt="example1" height="675" width="950"><hr>
Example 2:<br>
<img src="https://github.com/rootVIII/proxy_requests/blob/master/example_post_with_headers.png" alt="example2" height="1100" width="950">
