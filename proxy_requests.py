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
        self.__proxy_request()

    # recursively try socket until successful
    def __proxy_request(self):
        if len(self.sockets) > 0:
            current_socket = self.sockets.pop(0)
            proxies = {"https": "https://" + current_socket}
            try:
                request = requests.get(self.url, proxies=proxies)
                self.request = request.text
            except:
                print('hit next recursion level')
                self.__proxy_request()

    def __str__(self):
        return str(self.request)


if __name__ == "__main__":
    r = ProxyRequests("https://www.roboshout.com")
    print(r)
    # r = ProxyRequests.get("https://www.roboshout.com")
