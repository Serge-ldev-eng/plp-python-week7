# list_warmup.py - Stage 1: Warm up with list operations

# Create a shopping list
shopping_list = ["Milk", "Bread", "Eggs", "Apples"]

# Reading items by index
print("Shopping List:", shopping_list)
print(f"First item: {shopping_list[0]}")
print(f"Second item: {shopping_list[1]}")
print(f"Last item: {shopping_list[-1]}")

# Adding items
shopping_list.append("Chicken")
print(f"After adding Chicken: {shopping_list}")

# Inserting at specific position
shopping_list.insert(1, "Butter")
print(f"After inserting Butter at index 1: {shopping_list}")

# Slicing
print(f"First 3 items: {shopping_list[0:3]}")
