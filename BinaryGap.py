# 二进制数字两个1之间的最大间距
# 10010001 -> 3; 1111 -> 0; 1000 -> 0

def solution(N):
    # Implement your solution here
    binary_string = str(bin(N)[2:])
    gap = max_gap = 0
    for i in binary_string:
        if i == '0':
            gap += 1
        else:
            max_gap = max(gap,max_gap)
            gap = 0
    return max_gap
