#Write a function that accepts two strings and returns True if the two strings are
#anagrams of each other.
def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
str1="king"
str2="vickyS"
print(is_anagram(str1,str2))