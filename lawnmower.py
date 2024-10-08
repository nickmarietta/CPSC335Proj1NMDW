import sys

def lawnmower(n):
    list = [ "dark", "light"] * n
    left_index = 0
    right_index = 1
    n = len(list) 

    for x in range(int(n/2)):
        #traverses light left to right
        for i in range(left_index, n - right_index):
            if(list[i]=="dark" and list[i+1] == "light"):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        #makes start and end one index smaller
        right_index += 1
        left_index += 1
        #traverses right to left
        for j in range(n-right_index, left_index, -1):
            if(list[j]=="light" and list[j-1] == "dark"):
                tmp = list[j]
                list[j] = list[j-1]
                list[j-1] = tmp
        #makes start and end one index smaller
        right_index += 1
        left_index += 1

    return list 