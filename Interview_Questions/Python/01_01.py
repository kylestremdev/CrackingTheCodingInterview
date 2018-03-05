# Pg 90 - 1.1: Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Part 1 - Use of extra data structure
# Concept - Use dictionary to store previously visited characters,
#           lookup to see if character is in dictionary.
# Big O - Speed O(n) / Memory O(n)
def isUnique(string):
    # Delcare dictionary
    dic = {}

    # Iterate through letters
    for char in string:
        # Check if the character is already in the dictionary
        if char in dic:
            # Character exists, string is not unique return false
            return False
        # Store character in dictionary to track seen character
        dic[char] = True

    # If we iterate through all characters and have no dictionary matches,
    # string has no repeat characters; return true
    return True

print("----Function 1 Tests----")
print(isUnique("abc"))  # True
print(isUnique("aa"))   # False

# Part 2 - No additional data structures
# Concept - Brute force checking all characters against all others
def isUnique2(string):
    # Iterate through all characters
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            # Check if characters match
            if string[i] == string[j]:
                # If characters match, string is not unique; return false
                return False
    # Found no matches; return true
    return True

print("----Function 2 Tests----")
print(isUnique2("abc"))  # True
print(isUnique2("aa"))   # False
print(isUnique2("abcdefghijkll"))   # False
