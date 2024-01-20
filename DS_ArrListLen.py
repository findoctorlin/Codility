# 当前的value = 下一个链接的节点的 index
def solution(A):
    current = A[0]
    len_list = 1
    while current != -1:
        len_list += 1
        current = A[current]
    return len_list
