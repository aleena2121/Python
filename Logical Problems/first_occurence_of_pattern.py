def find_occurance(text,pattern):
    """
    This functions tells if the given patter exists in the string or not and if it exists at what position does it start

    Parameters:
    text: a string in which pattern is to be found
    pattern: the pattern to be found in the text

    Returns:
    If pattern exists in text then returns index else -1
    """
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1        
text = input("Enter text: ")
pattern = input("Enter pattern to find: ")
print(find_occurance(text,pattern))