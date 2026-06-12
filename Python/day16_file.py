try:
    file = open("abc.txt","r")
    print(file.read())
except:
    print("File Not Found")
    