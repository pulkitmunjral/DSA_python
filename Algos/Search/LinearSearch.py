def LinearSearch( list, value):
    flag = False
    for i in list:
        if i==value:
            flag = True
            break
    return flag


a = [1,2,3,4]

print(LinearSearch(a,5))