# Analysis and Design of Algorithms
# Program to implement Binary Search

# Binary Search using iteration
def binarySearchIterative(arr, key):
    start = 0
    end = len(arr) - 1
    # Start and end pointers shouldn't cross each other
    while start <= end:
        mid = (start + end)//2

        # If element is prsent at mid
        if(arr[mid] == key):
            return mid

        # If element is greater, ignore left half
        elif(arr[mid] < key):
            start = mid + 1

        # If element is smaller, ignore right half
        else:
            end = mid - 1

    # If we reach here, it means element isn't present in the array
    return -1

# Binary Search using recursion
def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    # Start and end pointers shouldn't cross each other
    if end >= start:
        mid = (end + start)//2
 
        # If element is present at the middle itself return mid element
        if arr[mid] == key:
            return mid
 
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > key:
            return binary_search(arr, start, mid - 1, key)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, end, key)
 
    else:
        # Element is not present in the array
        return -1

#Main Function
arr = [3,9,27,51,63,90]
print("Enter the element you want to find in the array: ")
num = int(input())
index = binarySearchIterative(arr, num) #Iterative function call
if(index == -1):
    print("Element not found")
else:
    print("Element is present at index", index)