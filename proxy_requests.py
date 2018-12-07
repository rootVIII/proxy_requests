#! /usr/bin/python3
import requests
import re
from requests.auth import HTTPBasicAuth


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.proxy = ''
        self.headers = {}
        self.file_dict = {}
        self.__acquire_sockets()
        self.status_code = ''
        self.proxy_used = ''
        self.raw_content = ''

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
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get()

    # recursively try proxy sockets until successful GET with headers
    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.get(self.url, timeout=3.0, proxies=proxies, headers=self.headers)
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get_with_headers()

    # recursively try proxy sockets until successful POST
    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url, json=data, timeout=3.0, proxies=proxies)
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(data)

    # recursively try proxy sockets until successful POST with headers
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
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_with_headers(data)

    # recursively try proxy sockets until successful POST with file
    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        files=self.file_dict,
                                        timeout=3.0,
                                        proxies=proxies)
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_file()

    def get_headers(self):
        return self.headers

    def set_headers(self, outgoing_headers):
        self.headers = outgoing_headers

    def set_file(self, outgoing_file):
        self.file_dict = outgoing_file

    def get_status_code(self):
        return self.status_code

    def get_proxy_used(self):
        return str(self.proxy_used)

    def response_to_file(self):
        from datetime import datetime
        file_name = 'proxy_requests_'
        file_name += datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        with open(file_name, 'wb') as file_out:
            file_out.write(self.raw_content)

    def get_raw(self):
        return self.raw_content

    def __str__(self):
        return str(self.raw_content)


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
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get()

    # recursively try proxy sockets until successful GET with headers (overrided method)
    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.get(self.url,
                                       auth=(self.username, self.password),
                                       timeout=3.0,
                                       proxies=proxies,
                                       headers=self.headers)
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.get_with_headers()

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
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post(data)

    # recursively try proxy sockets until successful POST with headers (overrided method)
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
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_with_headers(data)

    # recursively try proxy sockets until successful POST with file
    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
            try:
                request = requests.post(self.url,
                                        files=self.file_dict,
                                        auth=(self.username, self.password),
                                        timeout=3.0,
                                        proxies=proxies)
                self.headers = request.headers
                self.status_code = request.status_code
                self.raw_content = request.content
                self.proxy_used = current_socket
            except:
                print('working...')
                self.post_file()

    def __str__(self):
        return str(self.raw_content)


if __name__ == "__main__":
    # example post with headers
    r = ProxyRequests("https://postman-echo.com/post")
    r.set_headers({"name": "rootVIII", "secret_message": "7Yufs9KIfj33d"})
    r.post_with_headers({"key1": "value1", "key2": "value2"})
    print(r)
    print(r.get_headers())
    print(r.get_status_code())
    print(r.get_proxy_used())
