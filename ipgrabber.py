from requests import get

def ipGet():
    ip = get('https://api.ipify.org').text
    return ip
