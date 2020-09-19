import pytest
from socket import inet_aton
from uuid import uuid4
from proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
from proxy_requests import requests
# pytest -rsA tests/test_proxy_requests.py


@pytest.fixture
def henry_post_bucket():
    url = 'https://ptsv2.com/t/%s' % str(uuid4()).replace('-', '')
    requests.get(url)
    return url


def test_get():
    r = ProxyRequests('https://api.ipify.org')
    r.get()
    assert r.get_status_code() == 200
    try:
        inet_aton(r.__str__())
    except Exception:
        pytest.fail('Invalid IP address in response')
    print(r.get_proxy_used())


def test_get_with_headers():
    h = {'User-Agent': 'NCSA Mosaic/3.0 (Windows 95)'}
    r = ProxyRequests('https://postman-echo.com/headers')
    r.set_headers(h)
    r.get_with_headers()
    assert r.get_status_code() == 200
    assert 'headers' in r.get_json()
    print(r.get_proxy_used())


def test_post(henry_post_bucket):
    r = ProxyRequests(henry_post_bucket + '/post')
    r.post({'key1': 'value1', 'key2': 'value2'})
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(r.get_proxy_used())


def test_post_with_headers(henry_post_bucket):
    r = ProxyRequests(henry_post_bucket + '/post')
    r.set_headers({'name': 'rootVIII', 'secret_message': '7Yufs9KIfj33d'})
    r.post_with_headers({'key1': 'value1', 'key2': 'value2'})
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(r.get_proxy_used())


def test_post_file(henry_post_bucket):
    with open('/var/tmp/proxy_requests_testing.txt', 'w') as f_out:
        f_out.write('testing')
    r = ProxyRequests(henry_post_bucket + '/post')
    r.set_file('/var/tmp/proxy_requests_testing.txt')
    r.post_file()
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())


def test_post_file_with_headers(henry_post_bucket):
    with open('/var/tmp/proxy_requests_testing.txt', 'w') as f_out:
        f_out.write('testing')
    h = {'User-Agent': 'NCSA Mosaic/3.0 (Windows 95)'}
    r = ProxyRequests(henry_post_bucket + '/post')
    r.set_headers(h)
    r.set_file('/var/tmp/proxy_requests_testing.txt')
    r.post_file_with_headers()
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())


def test_get_with_basic_auth():

    url = 'https://postman-echo.com/basic-auth'
    r = ProxyRequestsBasicAuth(url, 'postman', 'password')
    r.get()
    assert r.get_status_code() == 200
    assert r.get_json()['authenticated']
    print(r.get_proxy_used())


def test_get_with_headers_basic_auth():
    url = 'https://postman-echo.com/basic-auth'
    h = {'User-Agent': 'NCSA Mosaic/3.0 (Windows 95)'}
    r = ProxyRequestsBasicAuth(url, 'postman', 'password')
    r.set_headers(h)
    r.get_with_headers()
    assert r.get_status_code() == 200
    assert r.get_json()['authenticated']
    print(r.get_proxy_used())


def test_post_with_basic_auth(henry_post_bucket):
    r = ProxyRequestsBasicAuth(henry_post_bucket + '/post', 'username', 'password')
    r.post({'key1': 'value1', 'key2': 'value2'})
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())


def test_post_with_headers_and_basic_auth(henry_post_bucket):
    r = ProxyRequestsBasicAuth(henry_post_bucket + '/post', 'username', 'password')
    r.set_headers({'header_key': 'header_value'})
    r.post_with_headers({'key1': 'value1', 'key2': 'value2'})
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())


def test_post_file_with_basic_auth(henry_post_bucket):
    with open('/var/tmp/proxy_requests_testing.txt', 'w') as f_out:
        f_out.write('testing')
    r = ProxyRequestsBasicAuth(henry_post_bucket + '/post', 'username', 'password')
    r.set_file('/var/tmp/proxy_requests_testing.txt')
    r.post_file()
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())


def test_post_file_with_headers_and_basic_auth(henry_post_bucket):
    with open('/var/tmp/proxy_requests_testing.txt', 'w') as f_out:
        f_out.write('testing')
    h = {'User-Agent': 'NCSA Mosaic/3.0 (Windows 95)'}
    r = ProxyRequestsBasicAuth(henry_post_bucket + '/post', 'username', 'password')
    r.set_headers(h)
    r.set_file('/var/tmp/proxy_requests_testing.txt')
    r.post_file_with_headers()
    assert r.get_status_code() == 200
    assert 'Thank you' in r.__str__()
    print(henry_post_bucket)
    print(r.get_proxy_used())
