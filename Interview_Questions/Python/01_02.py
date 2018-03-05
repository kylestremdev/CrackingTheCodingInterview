# Pg 90 - 1.2: Check Permutation
# Given two strings, write a method to decide
# if one is a permutation of the other.

# Concept - Use dictionary to store char and number of appearances of string one,
#           then use string two in attempt to zero out the dictionary
# Big O - Speed O(n + m) / Memory O(n)
def checkPerm(str1, str2):
    dic = {}

    for char in str1:       # Iterate through string one
        if char in dic:     # Check if char is in dictionary
            dic[char] += 1  # Increase number of appearances by 1

        dic[char] = 1       # Add char to dictionary if not already there

    for char in str2:       # Iterate through string two
        if char in dic:     # Check if char is in dictionary
            dic[char] -= 1  # Decrement char appearances by one
            if dic[char] == 0:
                dic.pop(char, None) # Delete char from dict if 0
        else:
            return False    # Character in string two does not exist in string
                            # one, therefore is not a permutation; return false

    if len(dic.keys()) == 0:    # Empty dictionary means permutation
        return True
    else:                       # Remainder in dic means no permutation
        return False

print("----Function Tests----")
print(checkPerm("a", "a"))      # True
print(checkPerm("ab", "a"))     # False
print(checkPerm("a", "ab"))     # False
print(checkPerm("kyle", "elyk"))# True
