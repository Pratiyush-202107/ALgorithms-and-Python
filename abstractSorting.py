# Program to construct an abstract class for the sorting
# methods that will force the inherited class to include
# all the relevant components like sort(), display(), etc.
from abc import ABC, abstractmethod # Abstract Base class

# Abstract sort class in which the constructor
# takes array as input to initialize it.
class abstractSort(ABC):
    def __init__(self, arr):
        self.arr = arr
        super().__init__()

    # Abstract method to sort the array, its implementation
    # must be mentioned further in the derived class else
    # the derived class also needs to be abstract.
    @abstractmethod
    def sort(self):
        pass
    
    def display(self):
        print("The array output from abstract class:", self.arr)

# Bubble Sort class derived from abstract class (abstractSort)
class bubbleSort(abstractSort):

    # Abstract method implementation
    def sort(self):
        l = len(self.arr)
        for i in range(l - 1):
            for j in range(0, l - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def bubbleSort_display(self):
        print("The sorted array via Bubble sort:", self.arr)
        
# Selection Sort class derived from abstract class (abstractSort)
class selectionSort(bubbleSort):

    # Abstract method implementation
    def sort(self):
        l = len(self.arr)
        for i in range(l):
            min_val_index = i
            for j in range(i + 1, l):
                if self.arr[min_val_index] > self.arr[j]:
                    min_val_index = j
                
            self.arr[i], self.arr[min_val_index] = self.arr[min_val_index], self.arr[i]

    def selectionSort_display(self):
        print("The sorted array via Selection Sort:", self.arr)


# Driver Code
arr = [2, 11, 9, 5, 7, 8, 13]

# Creating an object of class Selecttion sort
# and passing the array "arr" as argument
s = selectionSort(arr)

# Calling abstract class display function
# from the object of Selection sort class
s.display()

# Calling abstract method implemented in selectionSort class
s.sort()

# Calling display function of bubbleSort class
s.bubbleSort_display()

# Calling display function of selectionSort class
s.selectionSort_display()