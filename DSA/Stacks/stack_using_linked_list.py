class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        curr = self.head
        elements = []
        while curr is not None:
            elements.append(str(curr.data))
            curr = curr.next
        return " -> ".join(elements)

    def is_empty(self):
        return self.head is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            popped_value = temp.data
            del temp
            return popped_value


    def peek(self):
        if self.is_empty():
            print("No elements in stack")
        else:
            return self.head.data
    
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
print("Stack using linked lists : ")
print(st)

print("Popping element from stack : ")
st.pop()
print(st)

print(f"Topmost element in stack : {st.peek()}")