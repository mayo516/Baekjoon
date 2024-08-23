def solution(answers):
    # Patterns for each student
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1, s2, s3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            s1 += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            s2 += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            s3 += 1
    
    max_score = max(s1, s2, s3)
    answer = []

    if s1 == max_score:
        answer.append(1)
    if s2 == max_score:
        answer.append(2)
    if s3 == max_score:
        answer.append(3)
    
    return answer