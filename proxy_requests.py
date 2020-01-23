import requests
from random import randint
from re import findall
from traceback import print_exc
# rootVIII


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.request, self.proxy = '', ''
        self.proxy_used, self.raw_content = '', ''
        self.status_code = 0
        self.headers, self.file_dict = {}, {}
        self.json = None
        self.timeout = 8.0
        self.errs = ('ConnectTimeout', 'ProxyError', 'SSLError')
        self.acquire_sockets()

    # get a list of sockets from sslproxies.org
    def acquire_sockets(self):
        r = requests.get('https://www.sslproxies.org/')
        matches = findall(r"<td>\d+\.\d+\.\d+\.\d+</td><td>\d+</td>", r.text)
        revised = [m.replace('<td>', '') for m in matches]
        self.sockets = [s[:-5].replace('</td>', ':') for s in revised][:16]

    def set_request_data(self, req, socket):
        self.request = req.text
        self.headers = req.headers
        self.status_code = req.status_code
        self.raw_content = req.content
        self.proxy_used = socket
        try:
            self.json = req.json()
        except Exception:
            self.json = {}

    def rand_sock(self):
        return randint(0, len(self.sockets) - 1)

    def is_err(self, err):
        if type(err).__name__ not in self.errs:
            raise err

    @staticmethod
    def limit_succeeded():
        try:
            raise PoolSucceeded('Proxy Pool has been emptied')
        except PoolSucceeded:
            print_exc(limit=1)

    def get(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.get()
        else:
            self.limit_succeeded()

    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    timeout=self.timeout,
                    proxies=proxies,
                    headers=self.headers)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.get_with_headers()
        else:
            self.limit_succeeded()

    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post(data)

            else:
                self.limit_succeeded()

    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_with_headers(data)
        else:
            self.limit_succeeded()

    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_file()
        else:
            self.limit_succeeded()

    def post_file_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_file_with_headers()
        else:
            self.limit_succeeded()

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

    def get_raw(self):
        return self.raw_content

    def get_json(self):
        return self.json

    def __str__(self):
        return str(self.request)


class ProxyRequestsBasicAuth(ProxyRequests):
    def __init__(self, url, username, password):
        super().__init__(url)
        self.username = username
        self.password = password

    def get(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.get()
        else:
            self.limit_succeeded()

    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    proxies=proxies,
                    headers=self.headers)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.get_with_headers()
        else:
            self.limit_succeeded()

    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post(data)
        else:
            self.limit_succeeded()

    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    json=data,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_with_headers(data)
        else:
            self.limit_succeeded()

    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_file()
        else:
            self.limit_succeeded()

    def post_file_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self.rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files=self.file_dict,
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self.set_request_data(request, current_socket)
            except Exception as e:
                self.is_err(e)
                self.post_file_with_headers()
        else:
            self.limit_succeeded()


class PoolSucceeded(Exception):
    pass
