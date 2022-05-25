# COUNT WORDS IN A GIVEN TEXT 
# Users enter the text the want to count
text = input("Enter the text to be counted: ")
# split the text
splitted_words = text.split()
# find the length of the splitted words
counted_words = len(splitted_words)
# print out the number of words counted
print("There are ", counted_words, "words in the text given: ", text)
    