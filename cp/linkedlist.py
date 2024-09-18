class Node:
    value = None
    next = None

head = None

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        val = int(input("Enter value to insert: "))
        new_node = Node()
        new_node.value = val
        new_node.next = None
        
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node

    elif choice == '2':
        val = int(input("Enter value to delete: "))
        
        if head is None:
            print("List is empty.")
        elif head.value == val:
            head = head.next
        else:
            current = head
            while current.next:
                if current.next.value == val:
                    current.next = current.next.next
                    break
                current = current.next

    elif choice == '3':
        val = int(input("Enter value to search: "))
        found = False
        current = head
        
        while current:
            if current.value == val:
                found = True
                break
            current = current.next
        
        if found:
            print(f"{val} found in the list.")
        else:
            print(f"{val} not found in the list.")

    elif choice == '4':
        current = head
        if current is None:
            print("List is empty.")
        else:
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
