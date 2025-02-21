def flatten_list(l):
    if len(l) == 1: # Base case
        return l[0]
    else:
        return l[0] + flatten_list(l[1:]) # take the 1st sublist and then keep extending it with the 2nd sublist

l = [[1,2], [3,4], [5,6,7]]
print(flatten_list(l))