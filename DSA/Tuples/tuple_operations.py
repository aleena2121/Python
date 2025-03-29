# to create a tuple
tup1 = (1,2,3)
print("\nCreated a tuple: ", end="")
print(tup1)

# to create a tuple with different data types
tup2 = (1,2,3,"abc",[1,2,3])        # added different data types in the tuple - integers, string and a list
print("\nCreated a tuple with different data types: ", end="")
print(tup2)

# to unpack values of tuple in different variables
int1,int2,int3,string1,list1 = tup2        # using different valriables to unpack the values in the tuple
print("Unpacked values:", end=" ")
print(int1,int2,int3,string1,list1)

# to create a colon of a tuple
from copy import deepcopy
print("\nOriginal Tuple:",end=" ")
print(tup1)
copied_tuple = deepcopy(tup1)      # creating a copy of the original tuple
print("Copied Tuple:",end=" ")
print(copied_tuple)

# to find repeated items of a tuple
tup3 = (1,2,3,2,3,4)
print("\nTuple:",end=" ")
print(tup3)
print("Repeated items: ",end="")
repeated_items = set()              # creating a set to add the repeated items and to avoid duplicates
for i in tup3:
    if tup3.count(i) > 1:
        repeated_items.add(i)
print(repeated_items)

# to check if an element exists in the tuple
print("\nTuple:",end=" ")
print(tup2)
item_to_find = "abc"
print("Item to find: " + item_to_find)
if item_to_find in tup2:            # checks if the item is in the tuple or not and returns True of False accordingly
    print("Item exists in tuple!")
else:
    print("Item does not exist in tuple!")

# to convert a list to a tuple
print("\nList to be converted:", end=" ")
print(list1)
tup4 = tuple(list1)              # tuple() creates a tuple with whatever is passed as the argument
print("Converted to a tuple:", end=" ")
print(tup4)

# to remove an item from a tuple
# tuples are immutable, so we cannot remove any elements from it
# but we can create a new tuple but leaving some elements the tuple by slicing
print("\nOriginal Tuple:", end=" ")
print(tup1)
tup5 = tup1[:1] + tup1[2:]         # excluded index 1 using slicing
print("Removed index 1 by slicing: ", end="")
print(tup5)

# to slice the tuple
print("\nOriginal Tuple:", end=" ")
print(tup1)
print("Slicing the tuple from index 1 to end:", end=" ")
print(tup1[1:])       

# to reverse a tuple
print("\nOriginal Tuple:", end=" ")
print(tup1)
print("Reversed Tuple:", end=" ")
print(tup1[::-1])     # used reverse slicing