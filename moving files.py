import os

source = "yeet.txt"
destination =" C:\\Users\\lenye\\OneDrive\\Desktop\\yeet.txt"

try:
    if os.path.exists(destination):
        print("there is a file here")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+ "was not found")