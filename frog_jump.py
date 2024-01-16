def solution(X, Y, D):
    # D是步长
    quot, rem = divmod(Y-X,D)
    if rem == 0:
        return quot
    else:
        return quot+1
