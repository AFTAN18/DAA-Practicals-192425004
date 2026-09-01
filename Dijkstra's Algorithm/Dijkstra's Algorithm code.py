import heapq

n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

print("Enter edges (source destination weight):")

for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Enter source vertex: "))

distance = [float('inf')] * n
distance[start] = 0

pq = [(0, start)]

while pq:
    dist, u = heapq.heappop(pq)

    if dist > distance[u]:
        continue

    for v, weight in graph[u]:

        new_dist = dist + weight

        if new_dist < distance[v]:
            distance[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

print("Shortest distances:")

for i in range(n):
    print(start, "to", i, "=", distance[i])
