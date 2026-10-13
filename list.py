# shopping_list.py - Stage 2: Build the Manager

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"'{item}' has been added.")

def remove_item(item):
    # Safer to check 'in' before remove to avoid ValueError
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' not found in the list.")

def view_list():
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("\n--- Shopping List ---")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def main():
    while True:
        print("\n1. Add 2. Remove 3. View 4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_item(input("Item to add: ").strip())
        elif choice == "2":
            remove_item(input("Item to remove: ").strip())
        elif choice == "3":
            view_list()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
