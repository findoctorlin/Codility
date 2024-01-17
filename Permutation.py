# [4,1,3,2] [3,2,1] [6,3,2,1,4,5]
# 长度为N的数组，里面的数值是1 ~ N-1

def solution(A):
    target_set = set(range(1,len(A)+1))
    for element in A:
        try:
            target_set.remove(element)
        except KeyError:
            return 0
    return 1
# 用”移除法“，只要检测到KeyError(有不在target_set范围中的元素，return 0)
