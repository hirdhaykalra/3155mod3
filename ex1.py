#Worked with Haley Siharath
def my_function(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

my_list = [1, 2, 3, 2, 1, 4]
unique_list = my_function(my_list)
print(unique_list)