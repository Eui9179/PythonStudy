def solution(progresses, speeds):
    answer = []
    count = 0
    time = 1
    while(True):
        if progresses and progresses[0] + time * speeds[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        else:
            if count > 0:
                answer.append(count)
                if not progresses:
                    return answer
                count = 0
            time += 1

p = [93, 30, 55, 60, 40, 65]
s = [1, 30, 5, 10, 60, 7]
print(solution(p,s))
