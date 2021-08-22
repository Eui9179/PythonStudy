def solution(prices):
    answer=[0]*len(prices)

    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i]+=1
    return answer

        


j = [1,2,3,2,3,1]
print(solution(j))
'''
{1,2,3,2,3,1}로 해보라는데 그거도 제대로 {5,4,1,2,1,0}'''