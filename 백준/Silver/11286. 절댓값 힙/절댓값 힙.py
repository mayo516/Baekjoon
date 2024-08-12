import heapq as hq
import sys
# 빠른 입출력
input = sys.stdin.readline

pq = []

for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    
    else:
        if pq:
            print(hq.heappop(pq)[1])
        else:
            print(0)
