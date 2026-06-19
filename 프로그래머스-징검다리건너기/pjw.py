def can_cross(stones, k, mid):
    zero_stones = 0

    for stone in stones:
        if stone - mid < 0:
            zero_stones += 1
            if zero_stones == k:
                return False
        else:
            zero_stones = 0
    return True


def solution(stones, k):
    answer = 0
    min_p = 1
    max_p = max(stones)

    while True:
        if min_p > max_p: break

        mid = (min_p + max_p) // 2
        if can_cross(stones, k, mid):
            answer = mid
            min_p = mid + 1

        else:
            max_p = mid - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
