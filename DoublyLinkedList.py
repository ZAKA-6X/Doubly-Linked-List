
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self) -> None:
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node

    def display(self):
        if self.head == None:
            print('Your list is empty')
            return

        cur_node = self.head
        while cur_node != None:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next
        print('None')

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            count += 1
        return count

    def insert(self, data, index):
        if index < 0 or index > self.length():
            print('Your index is out of range')
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        cur_node = self.head
        count = 0
        while cur_node is not None and count < index - 1:
            cur_node = cur_node.next
            count += 1
        new_node.next = cur_node.next
        if cur_node.next is not None:
            cur_node.next.prev = new_node
        cur_node.next = new_node
        new_node.prev = cur_node

    def delete(self, data):
        if self.head is None:
            print('Your list is empty')
            return
        cur_node = self.head
        if cur_node.data == data:
            self.head = cur_node.next
            if self.head is not None:
                self.head.prev = None
            return
        while cur_node.next is not None and cur_node.next.data != data:
            cur_node = cur_node.next
        if cur_node.next is None:
            print('Your data is not in the list')
            return
        cur_node.next = cur_node.next.next
        if cur_node.next is not None:
            cur_node.next.prev = cur_node
            
    def get(self, data):
        cur_node = self.head
        count = 0
        while cur_node is not None and cur_node.data != data:
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            print('Your data is not in list')
            return -1
        return count

    def get_next(self, data):
        cur_node = self.head
        while cur_node is not None and cur_node.data != data:
            cur_node = cur_node.next
        if cur_node is None:
            print('Your data is not in list')
            return None
        if cur_node.next is None:
            return None
        print(cur_node.next.data)
        return
        
    def get_prev(self, data):
        if self.head == None:
            print('Your list is empty')
            return
        
        if self.head.data == data:
            print('Your data has not a prev')
            return 
        
        cur_node = self.head
        while cur_node != None and cur_node.data != data:
            cur_node = cur_node.next
        if cur_node == None:
            print('Your data is not in this list')
            return
        print(cur_node.prev.data)

# interface
my_node = DLL()
my_node.append(55)
my_node.append(12)
my_node.append(62)
my_node.append(87)
my_node.append(00)
my_node.display()
my_node.append(77)
my_node.display()
my_node.insert(44, 4)
my_node.display()
n = my_node.length()
print(n)
my_node.delete(62)
my_node.display()
i = my_node.get(44)
print(i)
my_node.get_next(87)
my_node.get_prev(77)
