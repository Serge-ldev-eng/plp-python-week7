# Week 7 Assignment: Hands-On Lab — Shopping List Manager

This repository contains the Week 7 assignment for Future Proof With Python.

Files:
- `list_warmup.py` - Warm-up practice with list creation, indexing, appending and slicing.
- `shopping_list.py` - Main manager that allows adding, removing and viewing shopping list items.
- `list_report.py` - Generates a smart report with totals, counts, sorted and reversed list.

Why check `in` before `remove()`?
It is safer to check `if item in list` before calling `list.remove()` because if the item does not exist, Python raises a `ValueError` and crashes the program. Checking first prevents the error and allows us to show a friendly "not found" message.
