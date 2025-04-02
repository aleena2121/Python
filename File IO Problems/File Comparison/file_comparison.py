import csv
import json

def file_comparison(file1,file2,file3):
    """
    This function writes into a new file the sentences which are different in 2 files

    Parameters - 
    file1,file2: the files from which content is to be compared
    file3: the file in which different sentences are to be entered
    
    """

    # # for .txt files
    # with open(file1,"r",encoding='utf-8') as file:
    #     content1 = file.readlines()

    # with open(file2,"r",encoding='utf-8') as file:
    #     content2 = file.readlines()
    
    # with open(file3,"w",encoding="utf-8") as file:
    #     for i in range(len(content1)):
    #         if content1[i] != content2[i]:
    #             file.write(f"Content in file 1 : {content1[i]}Content in file 2 : {content2[i]}\n")


    # # for csv files
    # with open(file1,"r",encoding="utf-8") as f1, open(file2,"r",encoding="utf-8") as f2:
    #     content1 = list(csv.DictReader(f1))
    #     content2 = list(csv.DictReader(f2)) 
    #  
    # fieldnames = ["File 1","File 2"]
    # with open(file3,"w",encoding="utf-8") as file:
    #     writer = csv.DictWriter(file,fieldnames=fieldnames)
    #     writer.writeheader()
    #     for i in range(len(content1)):
    #         if content1[i]['Sentence'] != content2[i]['Sentence']:
    #             writer.writerow({"File 1": content1[i]['Sentence'], "File 2": content2[i]['Sentence']})

    
    # for .json files
    with open(file1,"r",encoding="utf-8") as f1, open(file2,"r",encoding="utf-8") as f2:
        content1 = json.load(f1)
        content2 = json.load(f2)
        lines1 = content1['lines']
        lines2 = content2['lines']
    
    differences = []
    for line1, line2 in zip(lines1, lines2): 
        if line1 != line2:
            differences.append({"File 1": line1, "File 2": line2})

    with open(file3,"w",encoding="utf-8") as file:
            json.dump(differences,file,indent=4)


# file_comparison("file1.txt","file2.txt","result.txt")
# file_comparison("file1.csv","file2.csv","result.csv")
file_comparison("file1.json","file2.json","result.json")