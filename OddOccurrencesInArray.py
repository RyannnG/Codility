# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

from collections import defaultdict

def solution(A):
    # write your code in Python 2.7
    d = defaultdict()
    for i in A:
        d.setdefault(i, 0)
        d[i] += 1
        
    for i in d:
        if d[i] % 2 == 1:
            return i
            
    return -1