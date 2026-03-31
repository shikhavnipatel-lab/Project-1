class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack")

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get stack size
    def size(self):
        return len(self.stack)

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.stack):
                print(item)


# Main Program
if __name__ == "__main__":
    s = Stack()

    while True:
        print("\n--- Stack Operations Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = input("Enter value to push: ")
            s.push(value)

        elif choice == 2:
            popped = s.pop()
            if popped is not None:
                print(f"Popped element: {popped}")

        elif choice == 3:
            top = s.peek()
            if top is not None:
                print(f"Top element: {top}")

        elif choice == 4:
            s.display()

        elif choice == 5:
            print(f"Stack size: {s.size()}")

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
