def increasing_word_weights(sentence):
    """
    Function to find if the weights of words in the sentence are increasing or not
    """
    words = sentence.split()
    weights = [sum(ord(letter) for letter in word if letter.isalpha()) for word in words]
    for i in range(len(weights)-1):
        if weights[i]>weights[i+1]:
            return False
    return True

print(increasing_word_weights("All other roads."))