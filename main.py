class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


data = input("Введите элементы списка через пробел: ").split()
linked_list = LinkedList()
for item in data:
    linked_list.append(int(item))

print("Исходный список:")
linked_list.display()

linked_list.sort()

print("Отсортированный список:")
linked_list.display()