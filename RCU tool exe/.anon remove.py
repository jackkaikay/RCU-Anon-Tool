import os

dir_name = "C:/Users/jkay/Desktop/RCU-Anon-Tool/anon"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".anon"):
        newName = item[:-4]
        os.rename(item,newName)        


