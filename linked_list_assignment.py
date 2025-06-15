class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)



class LinkedListError(Exception):
    pass


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(res))

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def delete_nth_node(self, n):
        if not self.head:
            raise LinkedListError("List is empty")

        if n < 1:
            raise LinkedListError("Invalid index")

        if n == 1:
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(n - 2):
            if not curr.next:
                raise LinkedListError(f"Index {n} out of range")
            curr = curr.next

        if not curr.next:
            raise LinkedListError(f"Index {n} out of range")

        curr.next = curr.next.next

    def is_empty(self):
        return self.head is None


def test_linked_list():
    ll = LinkedList()

    print("Initial list:")
    ll.print_list()
    print(f"Length: {ll.get_length()}")
    print(f"Empty? {ll.is_empty()}")
    print()

    print("Adding elements:")
    for val in [10, 20, 30, 40, 50]:
        ll.add_to_end(val)
        print(f"Added: {val}")
    print("List after additions:")
    ll.print_list()
    print(f"Length: {ll.get_length()}\n")

    print("Deleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()
    print()

    print("Deleting 2nd node:")
    ll.delete_nth_node(2)
    ll.print_list()
    print()

    print("Deleting last node:")
    ll.delete_nth_node(ll.get_length())
    ll.print_list()
    print()

    while not ll.is_empty():
        ll.delete_nth_node(1)

    print("List after clearing all:")
    ll.print_list()

    try:
        ll.delete_nth_node(1)
    except LinkedListError as e:
        print(f"Error caught: {e}")
    
    for val in [100, 200, 300]:
        ll.add_to_end(val)

    print("\nList restored:")
    ll.print_list()

    for idx in [0, -1, 5, 10]:
        try:
            ll.delete_nth_node(idx)
        except LinkedListError as e:
            print(f"Error for index {idx}: {e}")
    
    print("\nFinal list:")
    ll.print_list()
    print(f"Final length: {ll.get_length()}")
    print("\n--- Done ---")


if __name__ == "__main__":
    test_linked_list()
