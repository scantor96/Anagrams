
import collections

def fileToList(file):
    word_list = []
    for line in file.readlines():
        if len(line) <= 21 and len(line) >= 3:
            nline = line.lower().strip()
            if nline not in word_list:
                word_list.append(nline)
    return word_list

def makeSortedList(alist):
    sorted_list = []
    for word in alist:
        sorted_word = "".join(sorted(word))
        sorted_list.append(sorted_word)
    return sorted_list

def checkRepeats(sorted_list):
    repeated_sets = [item for item, count in collections.Counter(sorted_list).items() if count > 1]
    repeated_sets = sorted(repeated_sets)
    return repeated_sets

def findAnagrams(repeated,alist):
    anagrams = {}
    anagram_groups = {}
    new_file = open("/Users/owner/Desktop/anagramstuff/AnagramSets.txt","a+")
    for word in alist:
        new_word = "".join(sorted(word))
        anagrams[word] = new_word
    for item in anagrams.items():
        alist = []
        if item[1] in repeated:
            alist.append(item[0])
            add_values_in_dict(anagram_groups,str(item[1]),alist)
    for item in anagram_groups.items():
        new_file.write(str(item[1]))
        new_file.write("\n")

def add_values_in_dict(dictionary,key,list_of_values):
    if key not in dictionary:
        dictionary[key] = list()
    dictionary[key].extend(list_of_values)
    return dictionary

file = open("/Users/owner/Desktop/anagramstuff/allwords.txt")
alist = fileToList(file)
sorted_list = makeSortedList(alist)
repeated = checkRepeats(sorted_list)
findAnagrams(repeated,alist)

    
