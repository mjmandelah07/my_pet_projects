# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(sorted_word1, sorted_word2):
    if sorted_word1 == sorted_word2:
       return True
    else:
        return False



# Ask for the words to be checked if they are anagrams from users
word1 = input("Enter the first word to find if it's anagram: ")
word2 = input("Enter the second word to find if it's anagram: ")

# check the two words given by users are of the same length
if len(word1) == len(word2):
    # change words to lower cases
    lower_word1 = word1.lower()
    lower_word2 = word2.lower()

    # sort the words alphabetically 
    sorted_word1 = sorted(lower_word1)
    sorted_word2 = sorted(lower_word2)
else:
    pass
    
try:
    # call the function
    print(find_anagrams(sorted_word1, sorted_word2))  
except:
    print("The two words entered are not of the same length, so the function is not called")    
    
