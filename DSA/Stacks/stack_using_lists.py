stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after appending : ")
print(stack)

print("Popping elements from the end : ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop())    IndexError: pop from empty list

print("Stack after popping all elements :")
print(stack)
