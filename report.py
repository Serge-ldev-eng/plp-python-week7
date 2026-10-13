# list_report.py - Stage 3: Smart Report

shopping_list = ["Milk", "Bread", "Eggs", "Milk", "Apples"]

# Generate smart report
print("--- Shopping List Smart Report ---")
print(f"Total items: {len(shopping_list)}")
print(f"Unique items: {len(set(shopping_list))}")
print(f"First item: {shopping_list[0]}")
print(f"Last item: {shopping_list[-1]}")

# Count occurrences
from collections import Counter
counts = Counter(shopping_list)
print("\nItem counts:")
for item, count in counts.items():
    print(f"- {item}: {count}")

# Sorted report
print(f"\nSorted list: {sorted(shopping_list)}")
print(f"Reversed list: {list(reversed(shopping_list))}")
