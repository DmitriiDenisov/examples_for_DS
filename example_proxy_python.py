import requests

##
# Date of test: 06.07.2019
# Location: Moscow, Russia
# Program output:
# <Response [403]>
# <Response [200]>
# <Response [200]>
# <Response [200]>

# Documentation on proxies for requests library:
# https://2.python-requests.org//en/latest/user/advanced/#proxies

# List of available proxy servers:
# https://hidemyna.me/en/proxy-list/
# http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all

# url = 'http://www.google.ru/'
url = 'http://rutracker.org'

# -------------
# Example 1. Connection without proxy:

q = requests.get(url)
print(q)  # if prints '<Response [200]>' => OK

# -------------
# Example 2. Connect via http proxy:

http_proxy = "118.140.151.98:3128"

proxyDict = {
    "http": http_proxy
}

r = requests.get(url, proxies=proxyDict)
print(r)

# -------------
# Example 3. Connect via https proxy:

https_proxy = "198.199.68.196:8080"

proxyDict = {
    "http": https_proxy,
    "https": https_proxy
}

r = requests.get(url, proxies=proxyDict)
print(r)
# -------------
# Example 4. Connect via socks proxy:

# First of all you need to run: 'pip install -U requests[socks]'
# Also may be required: 'pip install pysocks'

proxyDict = {
    "http": "socks5://108.61.164.105:33844",
    "https": "socks5://108.61.164.105:33844"

    # Another option with socks5:
    # "http": "socks5://67.205.146.29:1080",ok
    # "https": "socks5://67.205.146.29:1080"
}

q = requests.get(url, proxies=proxyDict)
print(q)
