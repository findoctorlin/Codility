# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# 长度为N的list中，数值从1 ~ N+1，找出missing value
def solution(A):
    full_A = range(1,len(A)+2)
    return sum(full_A) - sum(A)
