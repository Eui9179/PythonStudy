def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

'''
input                                               |   output
["leo", "kiki", "eden"]	                            |   ["eden", "kiki"]	
["marina", "josipa", "nikola", "vinko", "filipa"]   |   ["josipa", "filipa", "marina", "nikola"]
["mislav", "stanko", "mislav", "ana"]	            |   ["stanko", "ana", "mislav"]
'''

p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]	       

print(solution(p,c))

#모범답안
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]