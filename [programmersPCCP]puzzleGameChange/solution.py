def puzzle(diffs, times, limit, level):
    clear_time = 0
    prev_time = 0  # 이전 문제의 시간을 저장
    for idx, diff in enumerate(diffs):
        if diff <= level:
            clear_time += times[idx]
        else:
            clear_time += (diff - level) * (prev_time + times[idx]) + times[idx]
        
        if clear_time > limit:
            return False
        prev_time = times[idx]  # 현재 문제의 시간을 이전 시간으로 갱신
    return True

def solution(diffs, times, limit):
    start, end = 1, max(diffs)
    answer = -1  # 최적의 level을 저장

    while start <= end:
        mid = (start + end) // 2
        if puzzle(diffs, times, limit, mid):
            answer = mid  # 가능한 level 저장
            end = mid - 1  # 더 높은 level을 탐색
        else:
            start = mid + 1  # 낮은 level을 탐색

    return answer
