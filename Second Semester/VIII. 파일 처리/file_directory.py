import os

data = os.listdir("c:\\Users")
#print(data)
for d in data:
    print(d)
    print("is directory?: " + str(os.path.isdir(d)))
    print("is file?: " + str(os.path.isfile(d)))