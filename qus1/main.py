def sub_string(str1,str2):
    for i in str1:
        if i in str2:
            return "YES"
        return "NO"    

str1 = input("Enter the First String:")
str2 = input("Enter the Second String:")
print(sub_string(str1,str2))

#1. Write a program in which two strings are given and determine if they share a
#common substring. A substring may be as small as one character. The function
#returns either “YES” or “NO”.