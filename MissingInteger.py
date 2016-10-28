# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True

    for idx in xrange(len(seen)):
        if seen[idx] == False:
            return idx + 1

    return len(A)+1