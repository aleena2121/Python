from itertools import permutations

def find_permutations(number):
    """
    This function returns all the permutations of the given number

    Parameters
    ---
    number : the number given by the user

    Returns
    ---
    perm_list : a list of all permutations of the number
    """
    perm = list(permutations(str(number)))
    perm_list = [int(''.join(i)) for i in perm]
    return perm_list

num = int(input("Enter the number: "))
all_permutations = find_permutations(num)
print(f"Difference: {max(all_permutations)-min(all_permutations)}")