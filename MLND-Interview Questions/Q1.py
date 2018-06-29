'''Given two strings s and t, determine whether some anagram of t is a substring of s.
 For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False'''

def question1(s,t):

    #check string s and string t are equals
    if s==t:
        return True

    # if either of strings( s and t) is null
    if s==None or t==None:
        return False

    # for t should be substring of s . length of t should be smaller than s
    if len(t)>len(s):
        return False

    # Checking the character of t in s
    s=s.lower()
    t=t.lower()
    for character in t:
        if character in s:
            s = s.replace(character, '')
            t = t.replace(character, '')
    if not t:
        return True
    return False


# Test cases
print (question1("udAcity"," "))
print (question1(" "," "))
print (question1(" ","city"))
print (question1("udaCiTy","city"))
print (question1("udacity","ad"))


#Time Complexity =O(N) N is the number of element in the string
#Space Complexity =O(1)