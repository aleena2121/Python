def greet(name):
    """
    Function to greet a user

    Parameters: 
    name : string

    Returns :
    a statement, either greeting or invalid input 
    """
    if len(name)<3:
        print("Invalid Input")
    else:
        print("Hello " + name + ", How are you?")


name = input()
greet(name)
