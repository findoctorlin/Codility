https://app.codility.com/c/run/training5TWVPS-N5B/

def solution(A, K):
    # Implement your solution here
    if len(A) == 0:
        return A
    mod_K = K % len(A)
    return A[-mod_K:] + A[:-mod_K] #后mod_K个元素 + 其他元素
