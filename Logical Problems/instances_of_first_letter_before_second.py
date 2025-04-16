def check_instance(sentence,first_letter,second_letter):
    """
    This finctuion checks if all the instances of the first letter in the sentence appears before the second letter.
    
    Args:
    sentence : sentence to check in
    first_letter : first letter to check for
    sencond_letter : second letter to check for
    """
    pos_first_letter, pos_second_letter = 0,float("inf")
    for i in range(0,len(sentence)):
        if sentence[i] == first_letter:
            pos_first_letter = i
        elif sentence[i] == second_letter:
            pos_second_letter = i
        if pos_first_letter > pos_second_letter:
            return False
    return True

sentence = "a rabbit jumps joyfully"
first_letter = "u"
second_letter = "j"
print(check_instance(sentence,first_letter,second_letter))