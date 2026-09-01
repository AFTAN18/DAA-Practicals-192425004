def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        else:
            parent[root_y] = root_x
            rank[root_x] += 1


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (source destination weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))
rank = [0] * n

mst = []
total_cost = 0

for w, u, v in edges:

    if find(parent, u) != find(parent, v):

        mst.append((u, v, w))
        total_cost += w

        union(parent, rank, u, v)

print("Edges in MST:")

for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Minimum Cost =", total_cost)
