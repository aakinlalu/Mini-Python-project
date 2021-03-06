
# Filter Words Exercise
# =====================
# 
# This builds on the "filter words" exercise from the "Looping Patterns" lecture. You should considering doing that exercise first if you haven't done so already.
# 
# In this exercise, we want to print out the words from the following string that start with "o", ignoring case.


lyrics = '''My Bonnie lies over the ocean.
            My Bonnie lies over the sea.
            My Bonnie lies over the ocean.
            Oh bring back my Bonnie to me.
            '''

# Let's normalize case and remove punctuation
lyrics = lyrics.lower()
lyrics = lyrics.replace('.',"")
lyrics = lyrics.replace(',',"")


# Question 1
# ----------
# 
# This can be done with a `for` loop as follows:
# 
#     words = lyrics.split()
#     o_words = []
#     for word in words:
#         if word[0] == "o":
#             o_words.append(word)
# 
# Re-write this to use a list comprehension instead.


# We need to loop over all the words but are starting from a text with all the words together. 
# The first task is then to make a list of words:
words = lyrics.split()
# Now we can select those that start with the letter "o"
o_words = [word for word in words if word[0] == "o"]
# Of course we can combine the 2 step into one command. 
# Here we are also testing if a word starts with the letter "o" using the dedicated string 
# method 'startswith'
o_words = [word for word in lyrics.split() if word.startswith("o")]



print "words that start with 'o':"
print o_words


# Question 2
# ----------
# 
# Several words are repeated in the result generated by the list comprehension. Cast your list to another Python standard datastructure that will enforce uniqueness.


unique_o_words = set(o_words)
print unique_o_words


# Question 3
# ----------
# 
# If we are always going to collect all the words and then remove duplicates, we could build a set directly rather than going through a list. Use a set comprehension (or a generator expression if you are using an older version of Python) to produce the set of words that start with "o".


unique_o_words = {word for word in lyrics.split() if word.startswith("o")}
# generator expression version (for Python 2.6)
# unique_o_words = set(word for word in lyrics.split() if word.startswith("o"))



print "unique words that start with 'o':"
print unique_o_words


# Question 4
# ----------
# 
# Use a dictionary comprehension (or generator expression) to produce a dictionary whose keys are the words that start with "o" and whose values are the number of times the word is repeated.


o_word_frequencies = {word: lyrics.count(word) for word in lyrics.split() if word.startswith("o")}
# generator expression version
# o_word_dict = dict((word, lyrics.count(word)) for word in lyrics.split() if word.startswith("o"))



# or alternatively, and a little more efficiently
o_word_dict = {word: lyrics.count(word) for word in unique_o_words}
# generator expression version
# o_word_dict = dict((word, lyrics.count(word)) for word in unique_o_words)



print "unique words that start with 'o':"
print o_word_frequencies

