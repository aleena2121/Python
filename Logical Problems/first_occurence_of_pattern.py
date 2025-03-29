def find_occurance(text,pattern):
    """
    """
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1        
text = input("Enter text: ")
pattern = input("Enter pattern to find: ")
print(find_occurance(text,pattern))