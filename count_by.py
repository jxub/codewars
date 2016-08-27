def count_by(x, n):
    seq = []
    for num in range(x * n + 1):
        if num % x == 0 and num > 0:
            seq.append(num)
    return seq
