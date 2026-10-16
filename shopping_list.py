items = []
while True:
    choice = input("add / remove / show / done: ").lower()
    if choice == "done":
        break
    elif choice == "add":
        item = input("Add what? ")
        items.append(item)
        print(f"{item} added.")
    elif choice == "remove":
        # Guard before act - this is what gives marks
        item = input("Remove what? ")
        if item in items:
            items.remove(item)
            print(f"{item} removed.")
        else:
            print("That item is not on your list.")
    elif choice == "show":
        if not items:
            print("Your list is empty.")
        else:
            for i, it in enumerate(items, 1):
                print(f"{i}. {it}")
    else:
        print("Invalid choice. Use add / remove / show / done")
