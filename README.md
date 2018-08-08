## make an http GET/POST with a proxy scraped from https://www.sslproxies.org/
The ProxyRequests class first scrapes proxies from the web
<br><br>
Then it recursively attempts to make a request if the initial request with a proxy is unsuccessful
<br><br>
Runs on Linux and Windows-<b>may take a moment to run depending on current proxy</b>
<br><br>
Pass it a fully qualified URL when initializing an instance
<br><br>
The ProxyRequestBasicAuth subclass has a GET and POST that will override the Parent methods
<br><br>
<b>example GET:</b><br>
&emsp;&nbsp;r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example POST:</b><br>
&emsp;&nbsp;r = ProxyRequests("http://ptsv2.com/t/706cu-1533594868/post")<br>
&emsp;&nbsp;r.post({"key1": "value1", "key2": "value2"})<br><br>
<b>example POST with headers:</b><br>
&emsp;&nbsp;r = ProxyRequests("http://ptsv2.com/t/08iez-1533684032/post")
&emsp;&nbsp;r.set_headers({"name": "rootVIII"})
&emsp;&nbsp;r.post_with_headers({"key1": "value1", "key2": "value2"})<br><br>
<b>example GET with Basic Authentication:</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("https://postman-echo.com/basic-auth/", "postman", "password")<br>
&emsp;&nbsp;r.get()<br><br>
<b>example post with Basic Authentication</b><br>
&emsp;&nbsp;r = ProxyRequestsBasicAuth("url here", "username", "password")<br>
&emsp;&nbsp;r.post({"key1": "value1", "key2": "value2"})<br><br>
&emsp;&nbsp;print(r)<br>
&emsp;&nbsp;print(r.get_headers())<br>
&emsp;&nbsp;print(r.get_status_code())<br>
&emsp;&nbsp;print(r.to_json())<br>
&emsp;&nbsp;print(r.get_proxy_used())
<br><br>
The to_json() method is not intended to be used for a string of HTML<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<br><br>
coming soon.... a DELETE method, POST-file method, and possibly a POST-with-headers method as well.
<hr>
<b>Author: James Loye Colley  04AUG2018</b>
