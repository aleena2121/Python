def create_dictionary_from_string(s):    #  creates a dictionary by adding each character as key and the count of it as the related value
    dict = {}
    for i in s:
        dict[i] = s.count(i)
    print(dict)
    return dict

def print_in_table_format(dict):       # prints the dictionary in table format
    print("Character   | Count")
    for key,value in dictionary.items():
        print(key + "           | " + str(value))

        
# to track the count of the letters from the string and create a dictionary
s = "stringtocount"
print("String: ", end=" ")
print(s)
print("Dictionary: ",end=" ")
dictionary = create_dictionary_from_string(s)
print("\n")
print("Dictionary in table format: ")
print_in_table_format(dictionary)
print("\n")

# to get total count of a particular value associated with a key
list_of_dictionaries =  [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
print(list_of_dictionaries)
success_count = 0      
for dict in list_of_dictionaries:
    if dict['success'] == True:
        success_count+=1
print("Count of success = " + str(success_count))
print("\n")


# converting a list to a nested dictionary of keys
def list_to_dictionary(lst):
    if not lst:
        return {}
    return {lst[0]: list_to_dictionary(lst[1:])}   # recursion to repetatively add the list elements as nested dictionaries

list_ = [1,2,3,4,5]
print("List:", end=" ")
print(list_)
nested_dictionary = list_to_dictionary(list_)
print("Nested Dictionary: ", end=" ")
print(nested_dictionary)
print("\n")


# to check if multiple keys exist in a dictionary
dictionary1 = {1: "one",
              3: "three",
              6: "six",
              4: "four",
              2: "two",
              5: "five"
              }
keys_to_check = [1,2,3,4,5,6]
print("Keys to check : ", end=" ")
print(keys_to_check)
if all(key in dictionary1 for key in keys_to_check):   # all is a built-in function used to check if all iterables are True 
    print("All keys exist")
else:
    print("Some keys are missing")
print(dictionary1)
print("\n")


# to count number of items in a dictionary value that is a list
dictionary2 = {
    1 : ["one","1"],
    2 : "two",
    3 : ["three"]
}
count_of_list = 0
for value in dictionary2.values():
    if isinstance(value,list):    # isinstance returns True if the specified object is of the specified type
        count_of_list+=1
print(dictionary2)
print("Count of list values in dictionary : "+ str(count_of_list))