# function to find lowest common subsequence length using tabular form
def LCST(mainString, searchString):
    mainStringLength = len(mainString)
    searchStringLength = len(searchString)

    # Creating a 2-D matrix to store the tabular data
    matrix = [[0 for i in range(mainStringLength + 1)] for i in range(searchStringLength + 1)]
    for i in range (1, searchStringLength + 1):
        for j in range(1, mainStringLength + 1):
            # Check if the string elements are equal
            if searchString[i - 1] == mainString[j - 1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    # Printing the matrix
    for rows in matrix:
        print(rows)
    
    return matrix[searchStringLength][mainStringLength]


# Driver code
mainString = "abcdef"
searchString = "acfe"
m = len(mainString)
n = len(searchString)
Arr = [[0]*(m + 1)]*(n + 1)
print(f"Length of longest common subsequence in {mainString} is:", LCST(mainString, searchString))