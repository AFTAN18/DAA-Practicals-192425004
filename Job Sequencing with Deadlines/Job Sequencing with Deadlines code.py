n = int(input("Enter number of jobs: "))

jobs = []

print("Enter JobID Deadline Profit:")

for _ in range(n):
    job_id, deadline, profit = input().split()

    jobs.append((job_id, int(deadline), int(profit)))

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)

slots = [False] * max_deadline
result = [""] * max_deadline

total_profit = 0

for job_id, deadline, profit in jobs:

    for j in range(min(deadline, max_deadline) - 1, -1, -1):

        if not slots[j]:
            slots[j] = True
            result[j] = job_id
            total_profit += profit
            break

print("Selected Jobs:", " ".join(x for x in result if x))
print("Maximum Profit =", total_profit)
