class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def isEmpty(self):
        """
        This function checks if the given queue is empty or not
        """
        return self.front is None
    
    def print_queue(self):
        """
        Prints the queue
        """
        if self.isEmpty():
            print("Queue is Empty")
            return None
        curr = self.front
        while True:
            print(f"{curr.data} -> ",end="")
            if curr == self.rear:
                break
            curr = curr.next
        print("None")
            
    def enqueue(self,value):
        """
        This function add the given value to the front of the queue
        """
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        """
        This function removes an element from the rear
        """
        if self.isEmpty():
            print("No elements to delete")
            return 

        self.front = self.front.next

        if self.front is None:  # if empty make rear pointer also None
            self.rear = None

    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueue : ")
q.print_queue()

q.dequeue()
print("Queue after dequeue : ")
q.print_queue()