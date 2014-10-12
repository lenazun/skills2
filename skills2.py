from operator import itemgetter


string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):

	splitted = string1.split()
	dictionary = {}

	for i in splitted:
		dictionary[i] = dictionary.get(i, splitted.index(i))

	print dictionary

#count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	common = set(list1).intersection(set(list2))

	print list(common)

#common_items(list1, list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	
	dictionary = {}
	common = []

	for i in list1:
		dictionary.setdefault(i, 0)

	for i in list2:
		if dictionary.get(i,) != None:
			dictionary[i] += 1	

	for i in dictionary:
		if dictionary[i] > 0:
			common.append(i)

	print common

#common_items2(list1, list2)
		
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):

	pass


sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	
	print list(set(words))

#find_duplicates(words)

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	
	dictionary = {}
	sorted_list = []
	
	for i in words:
		dictionary.setdefault(i, len(i))

	for key, value in dictionary.iteritems():
		temp = [key, value]
		sorted_list.append(temp)

	sorted_list.sort()
	by_number = sorted(sorted_list, key=itemgetter(1), reverse = True)

	print by_number

word_length(words)	



"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
