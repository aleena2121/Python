from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after appending : ")
print(stack)

print("Popping elements from the end : ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack after popping all elements :")
print(stack)
