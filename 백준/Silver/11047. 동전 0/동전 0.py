n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
answer = 0
for coin in coins:
    answer += k//coin
    k %= coin
print(answer)