import json


student={
    "name":"Hemanth"
}

with open("student.json","w") as f:
    json.dump(student,f,indent = 4)
with open("student.json","r") as f:

    v = json.load(f)
print(v)

"""in this code there is not intialized of with statement 
to write and read  
not intialised json.load(f) and havn't printed."""