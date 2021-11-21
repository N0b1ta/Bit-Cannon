#!/usr/bin/env python3
import requests
print("==================================")
print("=           OneBitSec            =")
print("=                                =")
print("=    https://github.com/N0b1ta   =")
print("=                                =")
print("=        For learning only       =")
print("==================================")
target = input("please input target , example: http://127.0.0.1:8088/ :\n")
urls = target + "ws/v1/cluster/apps/new-application"
r = requests.post(urls)
responds = r.text
if "Cores" in responds:
	print("you found it!Try EXP")
elif "memory" in responds:
	print("you found it!Try EXP")
else:
	print("Nothing Here")
