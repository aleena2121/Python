import csv
import json
from itertools import islice

def read(file_input):
    """
    This function reads the given file in chunks (1024 bytes at a time)

    Parameters 
    ---
    file - file that needs to be read
    """

    # # for .txt files
    # with open(file_input,"r",encoding="utf-8") as file:
    #     while text := file.read(1024):
    #         print(text)

    # # for .csv files
    # with open(file_input,"r",encoding="utf-8") as file:
    #     text = csv.DictReader(file)
    #     while text := list(islice(text,10)):
    #         print(f"{text} \n")

    
    # for .json files
    with open(file_input,"r",encoding="utf-8") as file:
       for line in file:
            text = json.loads(line)  
            print(text)
# read("file.txt")
# read("file.csv")
read("file.json")