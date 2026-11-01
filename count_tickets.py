counts = {}

with open("tickets.txt") as file:
    for line in file:
        category = line.strip()
        counts[category] = counts.get(category, 0) + 1

sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)

for category, number in sorted_items:
    print(f"{category}: {number}")

