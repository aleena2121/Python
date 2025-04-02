import csv
import json

def column_extractor(data_file,column,output_file):
    """
    This function extracts the data under the column given in the csv file

    Parameters - 
    data_file: the csv file containing the data
    column: the column from which data needs to be extracted
    output_file: the file in which the data is to be written
    """

    # # for .csv files
    # col_data = []
    # with open (data_file,"r",encoding="utf-8") as file:
    #     data = csv.DictReader(file)
    #     for i in data:
    #         col_data.append(i[column])
    
    # with open (output_file,"w",encoding="utf-8") as file:
    #     for i in col_data:
    #         file.write(f"{i}\n")



    # for .json files
    col_data = []
    with open(data_file,"r",encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            col_data.append(i[column])

    with open(output_file,"w",encoding="utf-8") as file:
        json.dump(col_data,file,indent=4)
    

# column_extractor("data.csv","Department","departments.csv")
column_extractor("data.json","Name","name.json")