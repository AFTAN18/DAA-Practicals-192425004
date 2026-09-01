n = int(input("Enter number of items: "))

items = []

print("Enter value and weight for each item:")

for _ in range(n):
    value, weight = map(int, input().split())

    ratio = value / weight

    items.append((ratio, value, weight))

capacity = int(input("Enter knapsack capacity: "))

items.sort(reverse=True)

total_value = 0

for ratio, value, weight in items:

    if capacity >= weight:
        capacity -= weight
        total_value += value

    else:
        total_value += value * (capacity / weight)
        break

print("Maximum value =", total_value)
