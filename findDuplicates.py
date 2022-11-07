# function to find duplicate values in the list
def findDuplicates(list):
	size = len(list)
	duplicateList = []

    # for each element, check for its duplicates
	for i in range(size):
		for j in range(i + 1, size):
			if list[i] == list[j] and list[i] not in duplicateList:
				duplicateList.append(list[i])
	return duplicateList

# Driver Code
list1 = [12, 11, 10, 9, 11, 8, 12, 11]
print(findDuplicates(list1))