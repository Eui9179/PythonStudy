def cal_location(length, location):
    if location == 0:
        location = length - 1
    else:
        location -= 1
    return location

def solution(priorities, location):
    from collections import deque
    queue = deque(priorities)
    answer = 1
    while(True):
        if queue[0] == max(queue):
            if location == 0:
                return answer
            else:
                queue.popleft()
                location = cal_location(len(queue),location)
                answer += 1
        else:
            tmp = queue.popleft()
            queue.append(tmp)
            location = cal_location(len(queue),location)

p = [2, 1, 3, 2]	
l = 2 #return 1

p = [1, 1, 9, 1, 1, 1]	
l = 0 #return 5
print(solution(p,l))
