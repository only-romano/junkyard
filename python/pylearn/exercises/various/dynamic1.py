
cost = [0, 10000, 10000, 10000, 1, 1, 1, 1]
n = len(cost) - 1
G = [0] * (n + 1)
G[1] = cost[1]
G[2] = cost[2]
G[3] = cost[3]
for i in range(4, n+1):
    G[i] = min(cost[i] + G[i -1], cost[i] + G[i - 2], cost[i] + G[i -3])
print(G[n])