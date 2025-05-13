from queue import LifoQueue

stack = LifoQueue(maxsize=4)

print("Initial count of elements in stack")
print(stack.qsize())

stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)


print(f"Is Stack full : {stack.full()}")

print("Count of elements in stack after isertion")
print(stack.qsize())

print("Popping elements")
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())

print(f"Is Stack Empty : {stack.empty()}")