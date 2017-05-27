# lines 2- 9 just for designs
print("*" * 20)
print("*   Palindrome!!!  *")
print("*" * 20)

print(" "+"_" * 73)
print("| A palindrome is a word, phrase, number, or other sequence of characters |")
print("|  which reads the same backward as forward, such as madam or racecar     |")
print(" " + "_" * 73)

# ask the user to enter a string
print("\nTry it out!!!")
print("Enter a string (no SPACES) and the program will return the longest palindrome in the string")
user_input = input("-->").lower() # user input is stored here, convert it to all lowercase letters

palindromes_arr = []  # this list(array) holds the palindromes

# these nested loops combines characters in the passed string
# checks if the character sequence is a palindrome
# if it is a palindrome,
#  it stores the character sequence in a list (array)
for i in range(len(user_input)):  # loop from 0 to the number of characters in the string
    for j in range(0, i):  # loop from 0 to i
        palindrome = user_input[j:i + 1]  # combine characters from j to i+1

        # if the string is the same as the reverse of the string,
        # then the string is a palindrome
        # if  the character sequence is a palindrome, add it to the array
        if palindrome == palindrome[::-1]:  # string[::-1] gives the reverse of "string"
            palindromes_arr.append(palindrome)

# find the longest palindrome using max() function
# if there are multiple items of the same size/length, it returns the first one encountered
longest_palindrome = max(palindromes_arr, key=len)

# print out the palindromes and state the longest
print("The possible palindrome(s) in \n" + "*** " + user_input + " ***")
print("Are: " + "-->" + ", ".join(palindromes_arr) + "<--")
print("The longest palindrome is \n" + "*** " + longest_palindrome + " ***")