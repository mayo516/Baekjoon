import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline  #빠른입출력
N , M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a , b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a][b] = adj[b][a] = 1
ans = 0
chk = [False] * N


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)