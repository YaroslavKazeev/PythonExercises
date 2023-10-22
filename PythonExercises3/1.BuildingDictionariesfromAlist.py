# The code below contains a list of words. Build a dictionary that contains all these words as keys, and their quantities as values. Print the words with their quantities.

wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

wordlist.sort()
dictionary = {}
n=1
prevKey=""

for key in wordlist:
    if key == prevKey: n=n+1
    else: n=1
    dictionary[key]=n
    prevKey=key

for key in dictionary.keys():
    print ("{}:{}".format(key,dictionary[key]))