# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# 算出一个list在P位置分割了以后前后差值的最小值

def solution(A):
    if len(A) < 2:
        return 0
    s = sum(A)
    sum_left = 0
    min_diff = float('inf')

    for P in range(0,len(A)-1):
        sum_left += A[P]
        diff = abs(s - sum_left -sum_left)
        min_diff = min(diff, min_diff)
    
    return min_diff

#### ERROR: N^2 time ####
def solution(A):
    sum_left = 0
    sum_right = sum(A)
    min = sum_right - sum_left
    for P in range(1,len(A)):
        sum_left = sum(A[0:P])
        sum_right = sum(A[P:len(A)])
        res = abs(sum_left - sum_right)
        min = res if res < min or min is None else min

    return min

