import json
import csv

def file_update(file_name,key,value):
    """
    This function updates value of a specific key with a given value

    Parameters - 
    file_name: file to be updated
    key: the key at which the value is to be changed
    value: the changed value
    """

    # # for .csv files
    # with open(file_name,"r",encoding="utf-8") as file:
    #     content = json.load(file)

    # with open(file_name,"w",encoding="utf-8") as file:
    #     content[key] = value
    #     json.dump(content,file,indent=4)


    # # for .csv files
    # updated_rows = []

    # with open(file_name, "r", encoding="utf-8") as file:
    #     content = list(csv.DictReader(file))  
    #     fieldnames = content[0].keys()  
    #     for row in content:
    #         if key in row['Key']:  
    #             row[key] = value  
    #         updated_rows.append(row)
    # print(updated_rows)
    # with open(file_name, "w", encoding="utf-8", newline="") as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader() 
    #     writer.writerows(updated_rows)

    # for .txt file
    updated_lines = []
    
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(f"{key}:"): 
                updated_lines.append(f"{key}: {value}\n")  
            else:
                updated_lines.append(line)  
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)  
    

# file_update("file.json","age",26)
# file_update("file.csv","name","Aleena")
file_update("file.txt","age",26)