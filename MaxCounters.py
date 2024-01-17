# 有N = 5个初始值为0的counter，有数组A的长度为6
# 如果A[K]∈[1,N] -> 索引为A[K]-1的元素 += 1 ； 如果A[K] == N+1 -> 所有counters都设置为当前最大的counter值
''' A=[3,4,4,6,1,4,4]
    Counters:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
‘’‘
# 不要brutal!!! max的值=max(max, counters[A[K]-1])+1, 表示每次A[K]出现一次[1,N]范围内的值就更新一次max变量
# 难点在于：遍历A的时候，在对所有元素进行赋最大值操作的时候，要遍历一次counters数组，这里会让复杂度变成O(N^2) -> "想办法只遍历一次counters，写一个表达式去更新counters的值"(不要单纯的+=1)!!!!!!!!!!!!!!!!!!!!!!!
# 用一个叫bar的变量来记下 需要进行counter所有元素赋最大值操作 的时候的 increment量，这个bar也可以看做一个“基准量”for all

def solution(N, A):
    counters = [0] * N
    m = 0
    bar = 0
    for K in range(0,len(A)):
        if A[K] >= 1 and A[K] <= N:
            counters[A[K]-1] = max(bar, counters[A[K]-1]) + 1
            m = max(m, counters[A[K]-1])
        else:
            bar = m

    for i in range(0,len(counters)):
        if counters[i] < bar:
            counters[i] = bar

    return counters
