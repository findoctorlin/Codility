#  if the slice (i, j) is bounded then every slice (i + 1, j), (i + 2, j), . . . , (j, j) is bounded too

def solution(K, A):
    result = 0
    j = 0
    
    for i in range(len(A)):
        while j < len(A):
            if max(A[i:j+1]) - min(A[i:j+1]) <= K:
                j += 1
            else:
                break
        result += j - i
    
    return result
