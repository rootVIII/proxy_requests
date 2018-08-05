#! /usr/bin/python3
import requests
import re
import json


class ProxyRequests:
    def __init__(self, url):
        self.sockets = []
        self.url = url
        self.proxy = ""
        self.request = ""
        self.__acquire_sockets()

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
                request = requests.get(self.url, proxies=proxies)
                self.request = request.text
            except:
                print('working...')
                self.get()

    # recursively try proxy sockets until successful POST
    def post(self, data):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.post(self.url, data=data, proxies=proxies)
                self.request = request.text
            except:
                print('working...')
                self.post(self.url)

    def to_json(self):
        return json.dumps(self.request)

    def __str__(self):
        return str(self.request)

if __name__ == "__main__":
    # example GET
    r = ProxyRequests("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    r.get()
    print(r)
    print(r.to_json())
    # example POST
    # r = ProxyRequests("http://ptsv2.com/t/8s8j9-1533491569/post")
    # can pass a string or dict:
    # r.post("dump goes in toilet")
    # r.post({"key": "value", "one": "two"})
    # print(r)
