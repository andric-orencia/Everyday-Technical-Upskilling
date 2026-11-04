names = ["Ana", "Ben", "Cy"]
scores = [90, 75, 60]

total = 0
for score in scores:
    total = total + score
print(total)

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

for name, score in zip(names, scores):
    if score >= 70:
        print(name, "passed")
    else:
        print(name, "failed")
