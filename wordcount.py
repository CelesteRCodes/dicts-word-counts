# Write a program, wordcount.py, that opens a file and counts 
# how many times each space-separated word occurs in that file. 
# Your program should then print those counts to the screen.

# We’ve included a small file, test.txt, that you can use for testing 
# out your script. The file contains this poem...

# In addition to test.txt, we’ve provided a longer file, twain.txt, 
# which you can use to test out a longer input text.

# You may find it useful to switch to twain.txt to see 
# how your program performs when the text gets longer


# thought process:

# we need an import statement for test.txt and twain.txt
# may need to change 2nd variable to 'import test.txt' or import 'twain.txt'
# or use open(path)

# running through whole text and printing out each space seperated word 
# with how many times it occurs in the text


# def count_spaces(n, test.txt):
#     count = 0
#     for n in (test.txt):
#         if n == '_":              # are we counting the spaces
#             print(n, count += 1)
#         else:
#             return

# def count_spaces(n, path):
#    count = 0
#    for n in (test.txt):
#       if n == "": 
#           count += 1             
#           print(n, count)
#       else:
#           return

# count_spaces(n, 'test.txt')

# def word_count(n, path):
#     poem = open(path)             # opens path of inputh
#     count = 0 
#     for word in poem:
#         count(word)
#         print(count)

# can use split to get a list seperated to be iterated through
# instead of iterating through a string character by character

# for line in poem:
#     line = line.rstrip().split(" ")
#     print(line) 
# this prints out a list of each line of text

# need to create a dictionary for text to be stored in to loop through


def word_count(path):                           # open the file in read mode
     
    text = open(path, "r")                      # "r" is to read the file

     
    text_dict = dict()                          # create an empty dictionary

    
    for line in text:                           # loop through each line of the file 
        
        line = line.strip()                     # remove leading spaces and newline character 
         
        line = line.lower()                     # convert the characters in line to
                                                # lowercase to avoid case mismatch

         
        words = line.split(" ")                 # split line into words

        
        for word in words:                      # iterate over each word in line 
            
            if word in text_dict:               # check if the word is already in dictionary 
                                                 
                text_dict[word] = text_dict[word] + 1    # increment count of word by 1
            else: 
                
                text_dict[word] = 1             # add the word to dictionary with count 1

     
    for key in list(text_dict.keys()):          # print the contents of dictionary 
        print(key, ":", text_dict[key]) 

word_count('test.txt')



        