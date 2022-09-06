# function to find the position of the
# element at which partition is done
def partition(array, low, high):

  # choosing the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all the elements of array
  # and compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than or equal to pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the last greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where the partition is done
  return i + 1

# function to implement quickSort algorithm
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left and
    # element greater than pivot are on the right
    pivot = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pivot - 1)

    # recursive call on the right of pivot
    quickSort(array, pivot + 1, high)

# Driver code
array = [23,92,45,19,38,33]
print("Input array: ")
print(array)
size = len(array)
quickSort(array, 0, size - 1) #quickSort algorithm call
print("Sorted array: ")
print(array)