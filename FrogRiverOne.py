# 青蛙要从位置0跳到位置X+1，需要1 ~ X范围内的所有数字都出现在数组A[K]中，返回最早可以到对岸时候的索引K

def solution(X, A):
    target_set = set(range(1, X + 1))

    for K in range(len(A)):
        target_set.discard(A[K])
        if len(target_set) == 0:
            return K

    return -1

#同样利用set不能有重复元素的特点，遍历数组X，删除A[K]直至空
