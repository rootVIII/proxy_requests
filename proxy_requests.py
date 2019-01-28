#! /usr/bin/python3
import requests
import re
from requests.auth import HTTPBasicAuth


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.request, self.proxy = '', ''
        self.proxy_used, self.raw_content = '', ''
        self.status_code, self.try_count = 0, 15
        self.headers, self.file_dict = {}, {}
        self.__acquire_sockets()

    # get a list of sockets from sslproxies.org
    def __acquire_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    def __try_count_succeeded(self):
        message = "Unable to make proxied request. "
        message += "Please check the validity of your URL."
        print(message)

    def __set_request_data(self, req, socket):
        self.request = req.text
        self.headers = req.headers
        self.status_code = req.status_code
        self.raw_content = req.content
        self.proxy_used = socket

    # recursively try proxy sockets until successful GET
    def get(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    timeout=3.0,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.get()
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful GET with headers
    def get_with_headers(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    timeout=3.0,
                    proxies=proxies,
                    headers=self.headers
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.get_with_headers()
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful POST
    def post(self, data):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    timeout=3.0,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post(data)
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful POST with headers
    def post_with_headers(self, data):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    timeout=3.0,
                    headers=self.headers,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_with_headers(data)
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful POST with file
    def post_file(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    timeout=3.0,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_file()
        else:
            self.__try_count_succeeded()

    # recursively try until successful POST with file and custom headers
    def post_file_with_headers(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    timeout=3.0,
                    headers=self.headers,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_file_with_headers()
        else:
            self.__try_count_succeeded()

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
        return str(self.request)


class ProxyRequestsBasicAuth(ProxyRequests):
    def __init__(self, url, username, password):
        super().__init__(url)
        self.username = username
        self.password = password

    # recursively try proxy sockets until successful GET (overrided method)
    def get(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.get()
        else:
            self.__try_count_succeeded()

    # recursively try until successful GET with headers (overrided method)
    def get_with_headers(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    proxies=proxies,
                    headers=self.headers
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.get_with_headers()
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful POST (overrided method)
    def post(self, data):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    proxies=proxies)
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post(data)
        else:
            self.__try_count_succeeded()

    # recursively try until successful POST with headers (overrided method)
    def post_with_headers(self, data):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    headers=self.headers,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_with_headers(data)
        else:
            self.__try_count_succeeded()

    # recursively try proxy sockets until successful POST with file
    def post_file(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_file()
        else:
            self.__try_count_succeeded()

    # recursively try until successful POST with file and custom headers
    def post_file_with_headers(self):
        if len(self.sockets) > 0 and self.try_count > 0:
            current_socket = self.sockets.pop(0)
            proxies = {
                "http": "http://" + current_socket,
                "https": "https://" + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    auth=(self.username, self.password),
                    timeout=3.0,
                    headers=self.headers,
                    proxies=proxies
                )
                self.__set_request_data(request, current_socket)
            except Exception:
                self.try_count -= 1
                self.post_file_with_headers()
        else:
            self.__try_count_succeeded()

    def __str__(self):
        return str(self.request)
