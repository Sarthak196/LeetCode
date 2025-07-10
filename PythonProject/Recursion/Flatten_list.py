def flatten_list(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

l = [1,2,[3,4],5,[6,7,[8,9]]]
print(flatten_list(l))