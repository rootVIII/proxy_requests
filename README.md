## make an http GET with a proxy scraped from https://www.sslproxies.org/
<br><br>
Pass it a fully qualified URL when inializing an instance:
<br><br>
&emsp;&emsp;r = ProxyRequests("https://www.roboshout.com")<br>
&emsp;&emsp;print(r)

It first scrapes proxies from the web
<br><br>
Then it recursively attempts to make a request if the initial request with a proxy is unsuccessful
<br><br>
Runs on Linux and Windows- may take a moment to run depending on current proxy
<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<br><br>
POST coming soon as well as response in json format and HTTP Basic Auth
<hr>
<b>Author: James Loye Colley  04AUG2018</b>
