from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s) #used tuple as list can not be keys of a dictionary
    return list(res.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs)) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Create a default dict with a list as the default value. Iterate over the strings and create a list of 26 0s called
# count for each  string. Iterate through the characters of the string and increment the character's index in the count
# list by 1. Convert the count list to a tuple and use it as the key in the default dict and append the string to the
# list. Finally, return the values of the default dict as a list.