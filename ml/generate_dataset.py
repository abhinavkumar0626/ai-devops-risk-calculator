import random
import pandas as pd

data = []

for _ in range(100):
    files_changed = random.randint(1, 50)
    additions = random.randint(10, 2000)
    deletions = random.randint(5, 1500)
    duration = random.randint(60, 2000)

    # simple rule to simulate failure
    failed = 1 if files_changed > 30 and duration > 1000 else 0

    data.append([
        files_changed,
        additions,
        deletions,
        duration,
        failed
    ])

df = pd.DataFrame(data, columns=[
    "files_changed",
    "additions",
    "deletions",
    "duration",
    "failed"
])

df.to_csv("data/data.csv", index=False)

print("Dataset generated")
