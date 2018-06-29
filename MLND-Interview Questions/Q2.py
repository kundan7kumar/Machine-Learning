# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.
# NOTE: For quetions 1 and 2 it might be useful to have a function that returns all substrings...
# Check string is Palindrome or not
def isPal(s):
	# If string s is empty
	if not s:
		return True

	#if len of string is 1
	if len(s) == 1:
		return True

	# Else check the string is Palindrome
	if s[0] == s[-1]:
		return isPal(s[1:-1])
	return False


def question2(a):
	long_pal = ''

	# Check the string is palindrome
	if isPal(a):
		return a

	# Check all substrings whether it is palindrome.If palindrome and larger than longest_pal
	# make longest_pal the current substring
	i = len(a)
	j = 0
	while j != i:
		while i != j:

			if len( a[j:i] ) >= len( long_pal ) and isPal( a[j:i] ):
				long_pal = a[j:i]
			i=i- 1

		j =j+1
		i = len(a)

	return long_pal


# Test cases
print (question2("abcba"))
print (question2("forgeeksskeegfor"))
print (question2("a"))
print (question2(" "))
print (question2("qwertyyterq"))

#Time Complexity =O(N^2) where N length of string a
#Space Complexity =O(1)