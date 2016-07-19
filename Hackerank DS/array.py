#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
#print str(arr).strip('[]')
for i in arr:
    print i,
