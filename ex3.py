#Worked with Haley Siharath
def my_function(words):
    words = words.lower()
    finaldict = {}
    for i in words:
        if i != ' ':
            if i in finaldict:
                finaldict[i] = finaldict[i] + 1
            else:
                finaldict[i] = 1
    return finaldict
print(my_function(input("Enter a string: ")))
