# Function to print all permutations of a given string recursively
def permutate(str, answer):
    
    # If length of the string left is zero, it means we have reach the end therefore return
	if (len(str) == 0):
		print(answer, end = " ")
		return
	
    # Enter the loop and keep dividing the string and continue calling the function recursively
	for i in range(len(str)):
		ch = str[i]
		left_substring = str[0:i]
		right_substring = str[i + 1:]
		result = left_substring + right_substring
		permutate(result, answer + ch) # Recursive call

# Driver Code
answer = ""
my_str = input("Enter the string : ") # Taking input
print(f"All the possible permutations of {my_str} are: ")
permutate(my_str, answer) # Function call