# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    if A and len(A) > 1:
    
        sum1 = A[0]
        sum2 = sum(A[1:])
        
        min = abs(sum2 - sum1)
        
        for i in range(1, len(A)):
            # print sum1, sum2
            diff = abs(sum2 - sum1)
            # print diff
            sum1 += A[i]
            sum2 -= A[i]
            
            if diff < min:
                min = diff
    
        return min
        
    return abs(A[0])