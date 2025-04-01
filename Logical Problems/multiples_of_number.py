def multiples_of_num(num,length):
    """
    
    """
    multiples = []
    for i in range(1, length + 1):
        multiples.append(num*i)
    return multiples
num = int(input("Enter a number: "))
length = int(input("Enter the length: "))
print(multiples_of_num(num,length))