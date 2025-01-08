class Node:
    """Node has a value and next"""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # def append1(self, value):
    #     new_node = Node(value)
    #     temp = self.head
    #     prev = None
    #     while temp is not None:
    #         prev = temp
    #         temp = temp.next
    #     prev.next = new_node
    #     new_node.next = temp # None
    #     self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # if self.head is None:
        #     return
        # Empty list
        if self.length == 0:
            return None
        
        # Two or more items in the list
        temp = self.head
        prev = self.head
        while (temp.next):
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        # For one item in the list
        if self.length == 0:
            self.head = None
            self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
        # For two or more items in the list
            # temp = self.head
            # self.head = new_node
            # new_node.next = temp
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    # my_linked_list.append(5)
    # my_linked_list.append(7)
    # my_linked_list.append(8)
    my_linked_list.pop()
    my_linked_list.prepend(1)
    print(my_linked_list.print_list())
