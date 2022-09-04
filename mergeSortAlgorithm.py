# Function to implement mergeSort algorithm
def mergeSort(array):
	if len(array) > 1:
        # Finding the mid element about which the
        # partition of arrays has to be done
		mid = len(array)//2

		# Dividing the array int two subaArrays
		left_subArray = array[:mid]
		right_subArray = array[mid:]

		# Sorting the subArrays
		mergeSort(left_subArray)
		mergeSort(right_subArray)

        # Variables for maintaining current index of array and subArrays
		i = j = k = 0

		# Comparing the elements of subArrays and storing the smaller
        # one at current index of array until one of the subArray finish
		while i < len(left_subArray) and j < len(right_subArray):
			if left_subArray[i] < right_subArray[j]:
				array[k] = left_subArray[i]
				i += 1
			else:
				array[k] = right_subArray[j]
				j += 1
			k += 1

		# Storing the left elements of the unfinished subArray directly
		while i < len(left_subArray):
			array[k] = left_subArray[i]
			i += 1
			k += 1

		while j < len(right_subArray):
			array[k] = right_subArray[j]
			j += 1
			k += 1

# Function to print the array
def printList(array):
	for i in range(len(array)):
		print(array[i], end = " ")
	print()

# Driver Code
array = [23,12,49,36,27]
print("Input array: ", end = " ")
printList(array)
mergeSort(array) # Function call to mergeSort algorithm
print("Sorted array: ", end = " ")
printList(array)