# to create a set
set1 = {1,2,3,4}
print("\nCreated a set: ")
print(set1)

# to iterate over a set
print("\nIterating over the set: ")
for i in set1:
    print(i,end=" ")
print("\n")

# to add elements to a set
print("Adding 5 and 6 to the set: ")
set1.add(5)
set1.add(6)
print(set1)

# to remove elements from a set
print("\nRemoving 5 from the set: ")
set1.remove(5)         
print(set1)

# to check if a element is present in a set and then remove it
def remove_element(element,s):
    if element in s:
        s.remove(element)    # removes element from the set
        print("Successfully removed " + str(element) + " from string")
    else:
        print("Element not in set")
    return s

print("\nRemoving 5 from set: ")  # we can not remove 5 from set as it is not in the set
print(remove_element(5,set1))
print("\nRemoving 6 from set: ")
print(remove_element(6,set1))     # 6 will be removed

# intersecting sets
print("\nIntersecting 2 sets: ")
print("Set1: " ,end="")
print(set1)
print("Set2: " ,end="")
set2 = {3,4,5,6,7}
print(set2)
print("Intersection: ", end="")
set3 = set1.intersection(set2)  # returns thew common elements between set1 and set2
print(set3)

# union of sets
print("\nUnion of 2 sets: ")
print("Set1: " ,end="")
print(set1)
print("Set2: " ,end="")
print(set2)
print("Union: ", end="")
set4 = set1.union(set2)        # returns all the elements in set1 and set1
print(set4)

# set difference
print("\nDifference of 2 sets: ")
print("Set1: " ,end="")
print(set1)
print("Set2: " ,end="")
print(set2)
print("Difference: ", end="")
set5 = set1.difference(set2)    # returns the elements in set1 which are not in set2
                                # can be implemented like this also =>  set5 = set1 - set2
print(set5)

# symmetric difference
print("\nSymmetric difference of 2 sets: ")
print("Set1: " ,end="")
print(set1)
print("Set2: " ,end="")
print(set2)
print("Symmetric Difference: ", end="")
set6 = set1.symmetric_difference(set2)    # returns all elements except common elements
print(set6)

# clearing the set
print("\nClearing set 1: ")
set1.clear()
print("Set 1 : ", end="")
print(set1)

# implementing frozen sets
print("\nFrozen Set: ")
frozen_set = frozenset({1,3,4,5})
print(frozen_set)
# print(frozen_set[1])       
# this cannot be implemented as we cannot use indexing in sets or frozen sets

# to calculate maximum and minimum from a set
print("\nSet: ",end="")
print(set6)
print("Maximum in set: ", end="")
print(max(set6))                  # returns maximum from the set
print("Minimum in set: ", end="")
print(min(set6))                  # returns minumum from the set