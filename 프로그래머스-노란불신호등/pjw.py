def minimal_common(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


def solution(signals):
    plus = [sum(signal) for signal in signals]

    limit = plus[0]
    for p in plus[1:]:
        limit = minimal_common(limit, p)

    check = 0
    for time in range(2, limit + 1):
        for i in range(len(signals)):
            signal = signals[i]
            yellow_start = time % plus[i]
            if signal[0] < yellow_start <= signal[0] + signal[1]:
                check += 1
            else:
                break

        if check == len(signals):
            return time
        else:
            check = 0

    return -1
