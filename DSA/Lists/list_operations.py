import math

list1 = [1,2,3,4,5]
print("\nList: ",end='')
print(list1)

# to calculate sum of all elements in the list
print("Sum of elements of the list = " + str(sum(list1))) 

# to calculate product of all elemnte in the list
print("Product of elements of the list = " + str(math.prod(list1)))

# to get smallest no from the list
print("Smallest from the list: " + str(min(list1)))

# to count the number of strings where the string length is 2 or more and the first and last character are same from the given list of strings
list2 = ['abc', 'xyz', 'aba', '1221']
print("\nList: ",end="")
print(list2)
count = 0
for item in list2:
    if len(item)>=2:
        if item[0] == item[-1]:
            count += 1
print("Count of strings where the string length is 2 or more and the first and last character are same: "+ str(count))

# to sort list of tuples according to the last value of tuple
list3 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("\nList before sorting: ", end="")
print(list3)
list3.sort(key = lambda x:x[-1])           # lambda fucntion used to iterate through all the tuples and get the last value
print("List before sorting according to last elements of tuple: ", end="")
print(list3)

# to remove duplicates from a list
list4 = [1,1,4,5,3,4,2,1,4]
print("\nActual List: ", end="")
print(list4)
list4 = list(set(list4))                 # creating a set removes duplicates as a set can only contain unique values
print("After removing duplicates: ", end="")
print(list4)

# to copy list
list_to_copy = [10,20,30,40]
print("\nOriginal List: ", end="")
print(list_to_copy)
copied_list = list_to_copy.copy()         # creates a copy of the list
print("Copied List: ",end="")
print(copied_list)

# to find the list of words that are longer than n from a given list of words
list_of_words = ["Hi", "Hello", "Good", "Morning"]
print("\nOriginal List: ", end="")
print(list_of_words)
n = 4
print("Getting words that have length greater than " + str(n))
new_list = []
for i in list_of_words:
    if len(i) >= n:
        new_list.append(i)
print(new_list)

# to return True if two lists have at least one common member
list5 = [10,20,30,50]
list6 = [50,70,80,90]
print("\nFirst List: ",end="")
print(list5)
print("Second List: ",end="")
print(list6)
have_common = False           # using a boolean to track
for i in list6:
    if i in list5:
        have_common = True
        break                 # breaking loop when we find one element
if have_common == True:
    print("Both lists have at least one common number!")
else:
    print("No common number between both the lists")

# to delete specific indices from a list
list7 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("\nOriginal List:",end="")
print(list7)
print("Indices to delete:",end="")
indices_to_delete = [0,4,5]
print(indices_to_delete)
for i in range(len(indices_to_delete)-1,-1,-1):    # deleting in reverse order so that the it does not incorreclty delete
    del list7[indices_to_delete[i]]
print("Updated List: ",end="")
print(list7)

# to get all permutations of a list
from itertools import permutations            # in bulit package to find permutations
list8 = [1,2,3]
print("\nList:", end=" ")
print(list8)
perm = permutations(list8)
print("Permutations: ")
for i in perm:
    print(i)

# to find difference between sets
print("\nFirst List: ",end="")
print(list5)
print("Second List: ",end="")
print(list6)
print("Difference between sets: ")
print(set(list5)-set(list6))                # gets the difference between the sets

# to append a list to the second one
print("\nFirst List: ",end="")
print(list5)
print("Second List: ",end="")
print(list6)
for i in list5:
    list6.append(i)                         # adds the elements from one list to the end of the other
print("Appended List: ",end="")
print(list6)


# to check whether two lists are circularly identical
print("\nFirst List: ",end="")
print(list8)
list9 = [2,3,1]
print("Second List: ",end="")
print(list9)
combined_list = list8+list8                  # adding the same list twice so that we can find the other list in between
isIdentical = False                          # using boolean to keep track if it is identical
for i in range(len(combined_list)):
    if combined_list[i:i+len(list9)] == list9:      # using slicing in combined list to check if it is equal to the other list
        isIdentical = True
        break
if isIdentical:
    print("Yes, the lists are circularly identical!")
else:
    print("No, the lists are not circularly identical!")


# to find common elements between two lists
print("\nFirst List: ",end="")
print(list5)
print("Second List: ",end="")
list10 = [30,40,50,60]
print(list10)
print("Common elements: ",end='')
for i in list5:
    if i in list10:                  # checks if the current element of the first list is present in the other list
        print(i,end=" ")
print("\n")

# to split a list based on first character of word
from collections import defaultdict        # importing defalutdict so as to store a list corresponding to each letter
print("List of words: ", end="")
print(list_of_words)
dict = defaultdict(list)
for i in list_of_words:
    dict[i[0]].append(i)                   # creating a list corresponding to each letter and adding the words accordingly
print("Spliting according to first letter: ")
for key,values in dict.items():
    print(values)                        

#  to remove duplicates from a list of lists
list11 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("\nOriginal list:",end=" ")
print(list11)
list12 = []
for i in list11:
    if i not in list12:              # does not add i if it is already in the list
        list12.append(i)
print("List after removing duplicates: ",end="")
print(list12)