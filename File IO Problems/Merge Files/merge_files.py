def merge_files(file1,file2,output_file):
    """
    This function merges the text in two files and adds it into a new file

    Parameters - 
    file1,file2 - text files fto be merged
    output_file - the file in which we need to add the merged content
    """
    with open(file1,"r") as file:
        text1 = file.readlines()

    with open(file2,"r") as file:
        text2 = file.readlines()

    with open(output_file,"w") as file:
        for line1, line2 in zip(text1, text2):
            file.write(line1)
            file.write(line2)
        file.writelines(text1[len(text2):] or text2[len(text1):])

        
    
merge_files("merge_file1.txt","merge_file2.txt","merged.txt")