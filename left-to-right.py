import sys

list = [ "dark", "light"]*(int(sys.argv[1]))

for i in range(len(list)-1):
    for j in range(i, len(list)-1):
        if(list[j]=="dark" and list[j+1] == "light"):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list) 