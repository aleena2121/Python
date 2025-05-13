from queue import Queue

q = Queue(maxsize=5)

print(f"Initial no. of elements : {q.qsize()}")

q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(50)

print(f"Is queue full? : {q.full()}")
print(f"No. of elements after insertion : {q.qsize()}")

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print(f"Is queue empty? : {q.empty()}")
