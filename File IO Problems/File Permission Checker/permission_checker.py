import os

def check(file):
    """
    This functions check if the given file is readable, writable and executable.

    Parameters 
    ---
    file: the file to check
    """
    permissions = {
        "Readable": os.access(file, os.R_OK),
        "Writable": os.access(file, os.W_OK),
        "Executable": os.access(file, os.X_OK)
    }

    for perm, status in permissions.items():
        print(f"{perm}: {'Yes' if status else 'No'}")
    
check("file.txt")