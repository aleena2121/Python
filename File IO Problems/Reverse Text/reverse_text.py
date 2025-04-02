def reverse_line(input_file,output_file):
    """
    This functione reverses the text in the input file and writes the reversed text in the output file
    
    Parameters - 
    input_file: contains text to be reversed
    output_file: reversed text will be written here
    """
    with open(input_file,"r") as file:
        text = file.read()
    
    with open(output_file,"w") as file:
        file.write(str(text[::-1]))

reverse_line("reverse_text_input.txt","reverse_text_output.txt")