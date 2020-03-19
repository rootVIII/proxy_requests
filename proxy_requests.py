import requests
from random import randint
from re import findall
# rootVIII
# pycodestyle validated


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.request, self.proxy, self.used, self.raw, self.file_ = (
            '' for _ in range(5)
        )
        self.headers,  self.json = {}, {}
        self.status_code, self.timeout = 0, 3.0
        self.errs = ('ConnectTimeout', 'ProxyError', 'SSLError', 'ReadTimeout')
        self.empty_warn = 'Proxy Pool has been emptied'
        self._acquire_sockets()

    def _acquire_sockets(self):
        r = requests.get('https://www.sslproxies.org/')
        matches = findall(r"<td>\d+\.\d+\.\d+\.\d+</td><td>\d+</td>", r.text)
        revised = [m.replace('<td>', '') for m in matches]
        self.sockets = [s[:-5].replace('</td>', ':') for s in revised]

    def _set_request_data(self, req, socket):
        self.request = req.text
        self.headers = req.headers
        self.status_code = req.status_code
        self.raw = req.content
        self.used = socket
        try:
            self.json = req.json()
        except Exception:
            self.json = {}

    def _rand_sock(self):
        return randint(0, len(self.sockets) - 1)

    def _is_err(self, err):
        if type(err).__name__ not in self.errs:
            raise err

    def _limit_succeeded(self):
        raise Exception(self.empty_warn)

    def get(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.get(
                    self.url,
                    timeout=self.timeout,
                    proxies=proxies)
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.get()
        else:
            self._limit_succeeded()

    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.get_with_headers()
        else:
            self._limit_succeeded()

    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post(data)
        else:
            self._limit_succeeded()

    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_with_headers(data)
        else:
            self._limit_succeeded()

    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    proxies=proxies,
                    timeout=self.timeout,
                    files={'upload_file': open(self.file_, 'rb')})
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_file()
        else:
            self._limit_succeeded()

    def post_file_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files={'upload_file': open(self.file_, 'rb')},
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_file_with_headers()
        else:
            self._limit_succeeded()

    def get_headers(self):
        return self.headers

    def set_headers(self, outgoing_headers):
        self.headers = outgoing_headers

    def set_file(self, outgoing_file):
        self.file_ = outgoing_file

    def get_status_code(self):
        return self.status_code

    def get_proxy_used(self):
        return self.used

    def get_raw(self):
        return self.raw

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
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.get()
        else:
            self._limit_succeeded()

    def get_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.get_with_headers()
        else:
            self._limit_succeeded()

    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post(data)
        else:
            self._limit_succeeded()

    def post_with_headers(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
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
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_with_headers(data)
        else:
            self._limit_succeeded()

    def post_file(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files={'upload_file': open(self.file_, 'rb')},
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    proxies=proxies)
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_file()
        else:
            self._limit_succeeded()

    def post_file_with_headers(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(self._rand_sock())
            proxies = {
                'http': 'http://' + current_socket,
                'https': 'https://' + current_socket
            }
            try:
                request = requests.post(
                    self.url,
                    files={'upload_file': open(self.file_, 'rb')},
                    auth=(self.username, self.password),
                    timeout=self.timeout,
                    headers=self.headers,
                    proxies=proxies)
                self._set_request_data(request, current_socket)
            except Exception as e:
                self._is_err(e)
                self.post_file_with_headers()
        else:
            self._limit_succeeded()
