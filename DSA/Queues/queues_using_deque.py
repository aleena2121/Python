from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue after appending : ")
print(queue)

print("Popping elements from the end : ")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("Queue after popping all elements :")
print(queue)
