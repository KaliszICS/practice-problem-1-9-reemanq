
'''
    Lesson: String Manipulation
    Author: Mr. Kalisz
    Date Created: Sept 30, 2024
    Date Last Modified: Sept 30, 2024
'''

#Methods/Functions
#Function - A procedure that returns one thing
print(45)
#Method - A procedure associated with an object that returns one thing

#Upper - Creates a copy of a string with all uppercase characters

word = "Hello World"
wordUpper = word.upper()
print(word.upper()) #uses a copy, not the original
print(word) #unaffected by Upper

#Lower - Makes a copy that is lowercase

word = "Hello World"
wordUpper = word.lower()
print(word.lower()) #uses a copy, not the original
print(word) #unaffected by Upper

#len - length of the string in characters

print(len(word))


#INDEXES - Locations in a Data type

#First index is alwasy 0, the last index is always the length - 1
# H E L L O   W O R L D
# 0 1 2 3 4 5 6 7 8 9 10

#index

print(word.index("o")) #returns the index of the string
print(word.index("World")) #Gives the FIRST index of the string
print(word.index("l")) #First occurence of l
# print(word.index("h")) #runtime error when the value can't be found

#Splicing - Uses indexes create a substring (partial) copy of the original string

#variable[startingIndex: endingIndex]
#Starting Indexes - Inclusive, they include the index at the location
#Ending Index - Exclusive, it is NOT included in the substring

print(word[0:5])
print(word[6:15]) #Ending indexes that are larger than the last index, just continue to the end of string

#EndingIndex - StartingIndex = Length of the substring

print(word[2:10])

print(word[1:]) #Not specifying an ending index goes to the end of the string
print(word[:5]) #Not specifying a starting index starts at the beginning

print(word[3:-1]) #-1 is the last index of the string
print(word[-3:]) #Starts at the third LAST character

print(word[3]) #gives the single character at that index
# print(word[15]) #Go out of range on a single character, you get a runtime error
print(word[4:4]) #if the indexes are the same or cross over, you can an empty string

