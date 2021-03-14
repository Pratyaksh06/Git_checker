#!/usr/bin/python3

'''
before coding this is the point you need to remember:

1. You can do it, have patience and be consistent.

Task-1: Connecting to a "/.git" page of your target and it's subdomain
Task-2: Checking the HTTP status of that page
Task-3: Return the HTTP Status code
Task-4: If HTTP Status Code == 200 retrive the URL and the content

'''
import requests as re  # dealing with the requests.
import sys  # for command line input by the user ex python3 script.py example.com
import os  # importing this to have Subfinder tool for fast sub-domain enumeration

target = sys.argv[1]  # getting user input (target) from terminal


# using Subfinder to find domains on the provided target
os.system(f'subfinder -d {target} -silent -o {target}.txt >/dev/null 2>&1')


# creating file to store subdomains
f_ = open(f"{target}.txt", "r")
subdomainList_ = list(f_.read().split())
f_.close()
len_ = len(subdomainList_)

print(f"You got a total of {len} subdomains:\n", subdomainList_)

try:
    for i in subdomainList_:
        req = re.head(f"https://{i}/.git")
        if req.status_code == 200:
            print(f"https://{i}/.git :",req.status_code)
            data = f"https://{i}/.git".read()
            print(data)
        else:
            continue
except re.ConnectionError:
    print("Connection failed")


