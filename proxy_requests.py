#! /usr/bin/python3
import requests
import re
import json
from requests.auth import HTTPBasicAuth


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.proxy = ""
        self.request = ""
        self.headers = {}
        self.__acquire_sockets()
        self.status_code = ""
        self.proxy_used = ""

    # get a list of sockets from sslproxies.org
    def __acquire_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    # recursively try proxy sockets until successful GET
    def get(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.get(self.url, timeout=4.0, proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get()

    # recursively try proxy sockets until successful POST
    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.post(self.url, json=data, timeout=4.0, proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(self.url)

    def to_json(self):
        return json.dumps(json.JSONDecoder().decode(self.request))

    def get_headers(self):
        return self.headers

    def get_status_code(self):
        return self.status_code

    def get_proxy_used(self):
        return str(self.proxy_used)

    def __str__(self):
        return str(self.request)


class ProxyRequestsBasicAuth(ProxyRequests):
    def __init__(self, url, username, password):
        super().__init__(url)
        self.username = username
        self.password = password

    # recursively try proxy sockets until successful GET (overrided method)
    def get(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.get(self.url,
                                       auth=(self.username, self.password),
                                       timeout=4.0,
                                       proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get()

    # recursively try proxy sockets until successful POST (overrided method)
    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        json=data,
                                        auth=(self.username, self.password),
                                        timeout=4.0,
                                        proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(self.url)


if __name__ == "__main__":
    # ###### example GET ###### #
    r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    r.get()
    # ###### example POST ###### #
    # r = ProxyRequests("http://ptsv2.com/t/8kcv9-1533600808/post")
    # r.post({"key1": "value1", "key2": "value2"})
    # ###### example GET with Basic Authentication: ###### #
    # r = ProxyRequestsBasicAuth("https://postman-echo.com/basic-auth/", "postman", "password")
    # r.get()
    # ###### example POST with Basic Authentication ###### #
    # r = ProxyRequestsBasicAuth("url here", "username", "password")
    # r.post({"key1": "value1", "key2": "value2"})
    print('\n')
    print(r)
    print('\n')
    print(r.get_headers())
    print('\n')
    print(r.get_status_code())
    print('\n')
    print(r.to_json())
    print('\n')
    print(r.get_proxy_used())
