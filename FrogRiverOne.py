# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    
    d = dict()
    for i in range(len(A)):
            
        if A[i] <= X:
            d[A[i]] = i
            
        if len(d) == X:
            return i
    return -1