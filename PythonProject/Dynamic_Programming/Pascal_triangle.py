def generate(numRows):
    res = [[1]] # initialize the res with 1 which is the base case
    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0] # add 0 at the start and end of the last row of res for easy calculation
        row = []
        for j in range(len(res[-1]) + 1): # every next row is last_row's length + 1
            row.append(temp[j] + temp[j + 1]) # add the jth and j+1th element of temp and append it to row
        res.append(row) # append the row to res
    return res

print(generate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]