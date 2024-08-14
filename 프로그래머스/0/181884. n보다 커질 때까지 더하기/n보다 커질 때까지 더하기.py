def solution(numbers, n):
    answer = 0
    for a in numbers:
        answer += a
        if(answer>n):
            return answer
    
    