dictionary = {1: "one",
              3: "three",
              6: "six",
              4: "four",
              2: "two",
              5: "five"
              }

print("Original dictionary: ")
print(dictionary)

del dictionary[6]  #  deletes the key and the related value

print("Dictionary after deleting a key: ")
print(dictionary)  # prints dictonary without the deleted key