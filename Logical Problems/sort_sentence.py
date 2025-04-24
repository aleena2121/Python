def sort_sentence(sentence):
    """
    Function to return the sorted sentence by the word's location embedded within each word
    
    Args: 
    sentence: the sentence with locations embedded in words
    
    Returns:
    sorted_sentence_list: sorted sentence
    """
    sentence_list = sentence.split()
    digits = ["1","2","3","4","5","6","7","8","9"]
    sorted_sentence_list = [""]*len(sentence_list)
    for word in sentence_list:
        for letter in word:
            if letter in digits:
                word = word.replace(letter,"")
                sorted_sentence_list[int(letter)-1] = word
                break

    return " ".join(sorted_sentence_list)

print(sort_sentence("is2 Thi1s T4est 3a"))