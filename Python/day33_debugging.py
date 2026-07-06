with open("data.txt","r")as f:
    f.read()
    print(f)


"""the error in this code was writing 'w' and using file.read() 
it will give error so to use read() should be write 'r' in 
file opening line . and there was a another error at last line the 
file not closed properly it shoulb like this file.close()"""
