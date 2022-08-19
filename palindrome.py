# Program to print all unique substrings which are palindrome

#Palindrome class 
class Palindrome:
    def __init__(self, my_str): #Constructor
        self.string = my_str
        self.unique_substring = set()

    #Function to check the given string is palindrome or not
    def isPalindrome(self, start, end):
        # Start and end pointers shouldn't cross each other
        while(start < end):

            #Checking first and last element of string and then decrementing from both sides
            if(self.string[start] == self.string[end]):
                start += 1
                end -= 1
            else:
                return False
        # If we reach here, it means we have checked for all elements
        return True

    # Function to check unique substrings
    def checkSubstring(self):
        i = 0
        while i < len(self.string):
            j = len(self.string) - 1
            while (j > i):
                # If first and last elements are equal, then only proceed to check whether the substring is palindrome or not
                if (self.string[i] == self.string[j]):
                    # If the substring is palindrome, then store it in unique_substring set 
                    if self.isPalindrome(i, j):
                        self.unique_substring.add(self.string[i:j+1])
                        i = (i + j)//2
                        break
                j -= 1
            i += 1

# Main Function
string="malayalam"
my_str = Palindrome(string) # Object declaration
# Function call to Check all unique substrings if they're palindrome or not
my_str.checkSubstring()
# Printing the set of all unique substrings which are palindrome
print(my_str.unique_substring)