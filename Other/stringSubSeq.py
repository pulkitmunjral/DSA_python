# find if the string is a sub sequence of another string


def isSubSeq(parent, sub):

    i ,j = 0, 0

    while i < len(parent) and j < len(sub):
        if sub[j] == parent[i]:
            j+=1
        i+=1
    return j == len(sub)

print(isSubSeq('abcde','aec'))



