import heapq

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (source destination weight):")

for _ in range(e):

    u, v, w = map(int, input().split())

    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [False] * n

pq = [(0, 0)]

total_cost = 0

print("Edges in MST:")

while pq:

    weight, vertex = heapq.heappop(pq)

    if visited[vertex]:
        continue

    visited[vertex] = True
    total_cost += weight

    for w, neighbor in graph[vertex]:

        if not visited[neighbor]:
            heapq.heappush(pq, (w, neighbor))

print("Minimum Cost =", total_cost)
