#! /usr/bin/python3
import requests
import re


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


    # recursively try socket until successful
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

    def __str__(self):
        return str(self.request)

    # recursively try socket until successful POST
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


if __name__ == "__main__":
    # example GET
    #r = ProxyRequests("http://www.roboshout.com")
    #r.get()
    #print(r)

    # example POST
    r = ProxyRequests("http://ptsv2.com/t/8s8j9-1533491569/post")
    # can pass a string, dict:
    #r.post("dump goes in toilet")
    r.post({"key": "value", "one": "two"})
    print(r)