# 奇数个元素，non-empty, 只有一个元素在list中没有重复出现

# set()只放unuque元素
def solution(A):
    # Implement your solution here
    unpaired = set()
    for element in A:
        try:
            unpaired.remove(element) #从set中移除A的遍历值
        except KeyError:
            unpaired.add(element)
    return unpaired.pop()
