import requests


def hello_world():
    print("Hello World!")


def httpbin_get():
    response = requests.get("http://httpbin.org/get")
    return response
