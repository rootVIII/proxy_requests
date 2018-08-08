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
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.get(self.url, timeout=3.0, proxies=proxies)
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
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url, json=data, timeout=3.0, proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(self.url)

    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        json=data,
                                        timeout=3.0,
                                        headers=self.headers,
                                        proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_with_headers(self.url)

    def to_json(self):
        return json.dumps(json.JSONDecoder().decode(self.request))

    def get_headers(self):
        return self.headers

    def set_headers(self, outgoing_headers):
        self.headers = outgoing_headers

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
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.get(self.url,
                                       auth=(self.username, self.password),
                                       timeout=3.0,
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
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        json=data,
                                        auth=(self.username, self.password),
                                        timeout=3.0,
                                        proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(self.url)

    # recursively try proxy sockets until successful POST (overrided method)
    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        json=data,
                                        auth=(self.username, self.password),
                                        timeout=3.0,
                                        headers=self.headers,
                                        proxies=proxies)
                self.request = request.text
                self.headers = request.headers
                self.status_code = request.status_code
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_with_headers(self.url)


if __name__ == "__main__":
    # ###### example GET ###### #
    # r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    # r.get()
    # ###### example POST ###### #
    # r = ProxyRequests("http://ptsv2.com/t/08iez-1533684032/post")
    # r.post({"key1": "value1", "key2": "value2"})
    # ###### example POST with headers: ###### #
    # r = ProxyRequests("http://ptsv2.com/t/08iez-1533684032/post")
    # r.set_headers({"name": "rootVIII"})
    # r.post_with_headers({"key1": "value1", "key2": "value2"})
    # ###### example GET with Basic Authentication: ###### #
    # r = ProxyRequestsBasicAuth("https://postman-echo.com/basic-auth/", "postman", "password")
    # r.get()
    # ###### example POST with Basic Authentication ###### #
    # r = ProxyRequestsBasicAuth("url here", "username", "password")
    # r.post({"key1": "value1", "key2": "value2"})
    r = ProxyRequestsBasicAuth("http://ptsv2.com/t/08iez-1533684032/post", "james", "passwordy")
    r.set_headers({"name": "rootVIII"})
    r.post_with_headers({"key1": "value1", "key2": "value2"})
    print('\n')
    print(r)
    print('\n')
    print(r.get_headers())
    print('\n')
    print(r.get_status_code())
    print('\n')
    # print(r.to_json())
    print('\n')
    print(r.get_proxy_used())
