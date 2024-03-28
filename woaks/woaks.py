# iter, insert 기능 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init
        self.count = 0

    def __len__(self):
        return self.count

    def __repr__(self):
        s = ''
        currentnode = l.head.next
        while currentnode:
            s += f'{currentnode.data}, '
            currentnode = currentnode.next
        return f'<{s[:-2]}>'

    def __str__(self):
        s = ''
        currentnode = l.head.next
        while currentnode:
            s += f'{currentnode.data}, '
            currentnode = currentnode.next
        return f'<{s[:-2]}>'

    def __iter__(self):
        currentnode = l.head.next
        while currentnode:
            yield currentnode.data
            currentnode = currentnode.next

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1
    
    def insert(self, index, data):
        currentnode = l.head    
        for _ in range(index):
            currentnode = currentnode.next
        
        new_node = Node(data)   
        

        

        

l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l