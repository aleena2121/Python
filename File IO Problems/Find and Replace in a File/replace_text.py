import fileinput
import json
import csv

def replace_text(file_name,text_to_replace,replaced_text):
    """
    This function replaces the given word in the file in place with a new word given by the user

    Parameters
    ---
    file_name: the file inwhic text needs to be replaced
    text_to_replace: the text which is to be replaced
    replaced_text: the new text to be inserted
    """
    # # for .txt files
    # with fileinput.input(file_name, inplace=True) as file:
    #     for line in file:
    #         if text_to_replace in line:
    #             print(line.replace(text_to_replace,replaced_text))
    
    # # for .json files
    # with open(file_name,"r+",encoding="utf-8") as file:
    #     data = json.load(file)
    #     for key,value in data[0].items():
    #         if value == text_to_replace:
    #             data[0][key] = replaced_text 
    #     file.seek(0)
    #     json.dump(data,file,indent=4) 
    #     file.truncate()

    # for .csv files
    with open(file_name,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)  
        for row in data:
            for key in row:
                if row[key] == text_to_replace:
                    row[key] = replaced_text
        
    with open(file_name,"w",encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)


# replace_text("file.txt","John","Jake")
# replace_text("file.json","John","Jake")
replace_text("file.csv","John","Jake")