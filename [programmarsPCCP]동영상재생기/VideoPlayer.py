# 당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

# 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
# 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
# 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
# 동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 "mm:ss" -> 총 초(second)로 변환하는 함수
    def to_seconds(t):
        mm, ss = map(int, t.split(":"))
        return mm * 60 + ss

    # 초를 "mm:ss" 형식 문자열로 변환하는 함수
    def to_time_str(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02d}:{ss:02d}"

    # 주어진 값들을 초 단위로 변환
    video_total = to_seconds(video_len)
    current_pos = to_seconds(pos)
    op_s = to_seconds(op_start)
    op_e = to_seconds(op_end)

    # 오프닝 구간에 있을 경우 오프닝 끝 지점으로 이동
    if op_s <= current_pos <= op_e:
        current_pos = op_e

    for cmd in commands:
        if cmd == "prev":
            # 10초 전으로 이동 (최소 0초)
            current_pos = max(0, current_pos - 10)
        elif cmd == "next":
            # 10초 후로 이동, 만약 남은 시간이 10초 미만이면 영상 끝으로
            if current_pos + 10 > video_total:
                current_pos = video_total
            else:
                current_pos += 10

        # 이동 후 오프닝 구간에 있을 경우 오프닝 끝 지점으로 이동
        if op_s <= current_pos <= op_e:
            current_pos = op_e

    return to_time_str(current_pos)
