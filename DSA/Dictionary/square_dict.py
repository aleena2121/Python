def generate_dict(n):
    dictionary = {x:x*x for x in range(1,n+1)}   # creates a dictionayr with x as key and x*x as its value
    return dictionary

n = int(input("Enter a number : "))
print(generate_dict(n))