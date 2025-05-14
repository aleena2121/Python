def morse(s):
    """
    This function either converts a string of letters to morse code or morse code to string of letters
    
    Args: 
    s : a string containing either letters or a morse code

    Returns:
    result : string of letters or morse code
    """
    isMorse = True if s.count(".") > 0 else False
    morseCode = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
                "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
                "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
                "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
                "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
                " ":"....."}
    result = ""
    if isMorse:
        morseCode = {y:x for x,y in morseCode.items()}
        s = s.split()
        return "".join(morseCode[i] for i in s)
    else:
        for i in s:
            return " ".join(morseCode[i.upper()] for i in s)


print(morse("F Mueller"))
print(morse(".--- --- .... -. ..... ..-. ..... -.- . -. -. . -.. -.--"))
