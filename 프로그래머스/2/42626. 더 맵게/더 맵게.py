import heapq as hq


def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while len(scoville):
         if len(scoville) == 1:
            if  scoville[0] < K:
                return -1
         # hq.heapify(scoville)
         h1 = hq.heappop(scoville)
         if  h1 >= K:
            return answer
         # print(h1)
         # print(h2)
         h2 = hq.heappop(scoville)
         hq.heappush(scoville, h1 + h2 * 2)
         answer += 1
         # print(scoville)
         