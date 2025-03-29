dictionary = {1: "one",
              3: "three",
              6: "six",
              4: "four",
              2: "two",
              5: "five"
              }

sorted_dictionary_ascending = dict(sorted(dictionary.items()))          # sorts the dictionary according to its keys in acsending order
sorted_dictionary_descending = dict(sorted(dictionary.items(),reverse=True))   # sorts the dictionary according to its keys in decsending order
print("Ascending : ")
print(sorted_dictionary_ascending)
print("Descending : ")
print(sorted_dictionary_descending)