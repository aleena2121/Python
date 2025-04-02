import string
import json
import csv
from collections import Counter

def word_frequency_counter(input,output):
    """
    This function writes into a new file the words and their corresponding counts in the input file

    Parameters - 
    input_file : the input file containing words
    output_file: file in which we need to write the count of words
    """

    # # for .txt files

    # with open(input,"r") as file:
    #     words = file.read().lower()
    #     s = ''.join(char if char not in string.punctuation else " " for char in words)
    #     s = s.split()

    # word_count = Counter(s)

    # with open(output,"w") as file:
    #     for word,count in word_count.items():
    #         file.write(f"{word} : {count}\n")



    # for .json files

    # with open(input,"r") as file:
    #     content = json.load(file)
    #     words = content['text'].lower()
    #     s = ''.join(char if char not in string.punctuation else " " for char in words)
    #     s = s.split()

    # word_count = Counter(s)

    # with open(output,"w") as file:
    #     json.dump(word_count,file,indent=4)



    # for .csv files
    
    with open(input,"r") as file:
        content = csv.DictReader(file)
        words = ""
        for i in content:
            words += i['Text'].lower()
        s = ''.join(char if char not in string.punctuation else " " for char in words)
        s = s.split()

    word_count = Counter(s)

    with open(output,"w") as file:
        writer = csv.writer(file)
        writer.writerow(["Word","Count"])
        for word,count in word_count.items():
            writer.writerow([word,count])

# word_frequency_counter("word_frequency_counter_input.txt","word_frequency_counter_output.txt")
# word_frequency_counter("input.json","output.json")
word_frequency_counter("input.csv","output.csv")