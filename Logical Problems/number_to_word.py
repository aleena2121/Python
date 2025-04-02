def number_to_word(num):
    """
    This function converts the given number to words

    Parameters - 
    num: number to convert to word

    Returns - 
    word: a string containing word representation of the number
    """
    dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
            10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
            17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",
            50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand",100000:"lakh",10000000: "crore"}
    
    if num in dict:
        return dict[num]
    
    word = ""
    num_str = str(num)
    length = 10 ** (len(num_str) - 1)
    
    for i in range(len(num_str)):
        current_digit = int(num_str[i])
        
        if current_digit == 0:
            length = length // 10
            continue
            
        if current_digit == 1 and (length == 100 or length == 1000 or length == 100000 or length == 10000000):
            word += dict[current_digit] + " " + dict[length] + " "
            length = length // 10
            continue

        if (length == 10 and current_digit >= 2) or (length == 10000 or length == 1000000):
            word += dict[current_digit * 10] + " "
            length = length // 10
            continue
            
        if current_digit * length in dict:
            word += dict[current_digit * length] + " "
        else:
            word += dict[current_digit]
            if length > 10 and length in dict:
                word += " " + dict[length] + " "
            else:
                word += " "
                
        length = length // 10
    
    return word.strip()




num = int(input("Enter number: "))
print(number_to_word(num))