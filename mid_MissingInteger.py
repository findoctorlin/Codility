def solution(A):
    min_integer = 1
    unique_A = set(element for element in A if element > 0)

    for element in unique_A:
        if element == min_integer:
            min_integer += 1
    return min_integer
