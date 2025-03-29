def add(key,value,dict):
    dict[key] = value    # mapping the value to the key
    return dict

dict = {}    # initializing empty dictionary
add(0,10,dict)
add(1,20,dict)
add(2,30,dict)
print(dict)