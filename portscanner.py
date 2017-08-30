#!/usr/bin/python

import requests
import sys

def scan(pr, p):
    IP=sys.argv[1]
    url = pr + IP + ':' + str(p)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print 'Found open port =  ' + url

    except:
        pass


def values():
    portList = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 443, 445, 1433, 500, 2082, 2083, 2086, 2087, 2095,
                2096,3306, 3389, 5900, 8080, 8880, 8443, 9998, 4643, 9001, 4489]


    http = 'http://'
    https = 'https://'



    for port in portList:
        scan(http, port)
        scan(https, port)


if __name__=='__main__':
    values()
