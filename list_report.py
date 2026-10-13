items = ["milk", "bread", "butter", "orange juice", "rice"]

# Step 6: Numbered list + count len > 4
counter = 1
count_long = 0
for item in items:
    print(f"{counter}. {item}")
    counter += 1
    if len(item) > 4:
        count_long += 1

print(f"Items with more than 4 letters: {count_long}")

# Step 7: Longest name - best-so-far pattern
longest = ""
for item in items:
    if len(item) > len(longest):
        longest = item
print(f"Longest item: {longest}")
