from itertools import combinations


def solution(n, q, ans):
    nums = [i for i in range(1, n + 1)]
    possible_cases = list(combinations(nums, 5))
    answer = 0

    for case in possible_cases:
        check = 0
        for i in range(len(q)):
            cnt = 0
            case_set = set(case)
            query_set = set(q[i])

            cnt += len(case_set & query_set)

            if cnt == ans[i]:
                check += 1

        if check == len(q):
            answer += 1

    return answer
