fruits = ["mango", "banana", "orange", "apple", "grape"]

# Step 1: Accesslist.warmu.py
print(fruits[0])
print(fruits[-1])

# Step 2: Append, remove, measure - print after each change
print(f"Original list: {fruits}")

fruits.append("pineapple")
print(f"After append: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

print(f"Length: {len(fruits)}")
