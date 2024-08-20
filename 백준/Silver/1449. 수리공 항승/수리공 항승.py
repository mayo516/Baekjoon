n , l = map(int, input().split())
coord = [False] * 1001 #0부터 1000이기 때문에 1001
for i in map(int, input().split()):
    coord[i] = True

answer = 0 
x = 0 #점프를 해서 지나가야 되기 때문에 for문 돌기보단 지정 좌표로 부터 
while x < 1001:
    if coord[x]: #TRUE면 
        answer +=1 
        x += l #테이프 길이만큼 건너뛰기
    else:
        x +=1

print(answer)
    
