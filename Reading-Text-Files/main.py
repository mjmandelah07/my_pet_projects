# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# funtion to read the file "story.txt"
def read_file_content(str):
    # open the file in a read mode
    text = open(str, "r")
    # read the content of the file
    return text.read()


# funtion to count each words in the file 
def count_words():
    # ask for file name from the user
    text_file = input("Enter the file name you want to count the words from: ")
    # call the funcion that reads the file
    text1 = read_file_content(text_file)
    
    # count the words in a dictionary
    counts = dict()
    
    # split the words to count them
    words_in_story_text = text1.split()

    # iterate over the words that was splited in (words_in_story_text)
    for word in words_in_story_text :
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(count_words())