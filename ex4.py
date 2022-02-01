#Worked with Haley Siharath
def inputadder():
    listofnum = []
    i=0
    while i < 5:
        print(f"enter input {i+1}")
        listofnum.append(input())
        if listofnum[i].isnumeric():
            i += 1
        else:
            print("You didn't input an int! Try again: ")
            listofnum.pop(i)
    final = 0
    for x in listofnum:
        final = final + int(x)
    return final

answer = inputadder()
print(answer)

#Sources: https://www.delftstack.com/howto/python/user-input-int-python/
#isnumeric() checks if input is integer and returns true if it is