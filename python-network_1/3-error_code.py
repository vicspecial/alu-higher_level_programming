#!/usr/bin/python3
"""2-post_email.py"""


import urllib.request
import urllib.error
import sys

def fetch_url(url):
    """ this is documented"""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    """ this is also documented"""
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url) 
