import json
import csv
def log_error(input_file,error_file):
    """
    This fucntion writes into another file all the error logs
    """

    # # for .txt file
    # with open (input_file,"r") as file:
    #     logs = file.readlines()
    
    # with open (error_file,"w") as file:
    #     for log in logs:
    #         if "ERROR" in log:
    #             file.write(log)



    # # for .json files
    # error_logs = []
    # with open(input_file,"r",encoding="utf-8") as file:
    #     logs = json.load(file)
    #     for i in logs:
    #         if i['level'] == "ERROR":
    #             error_logs.append(i)
    # with open(error_file,"w",encoding="utf-8") as file:
    #     json.dump(error_logs,file,indent=4)



    # for .csv files
    error_logs = []
    with open(input_file,"r",encoding="utf-8") as file:
        logs = csv.DictReader(file)
        fieldnames = logs.fieldnames 
        for log in logs:
            if log['level'] == "ERROR":
                error_logs.append(log)
    
    with open(error_file,"w",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(error_logs)
        
# log_error("logs.txt","error.txt")
# log_error("logs.json","error.json")
log_error("logs.csv","error.csv")