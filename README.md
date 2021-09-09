# Anagrams

-I make puzzles entirely populated with valid anagrams and I often get comments wondering how I am able to do that.
-My method has been to only use a wordlist of anagrams to fill a grid. I used to add to the list manually, putting in anagrams I noticed in the wild. But as the puzzles got bigger, those lists became too small for my purposes, so I wrote a little Python code to do that work for me.
-I use a lot of different wordlists when I make puzzles, I've linked to some of the larger ones below. I've attached the code I used to find valid pairs. 
-I've uploaded `allwords.txt`, which is the list of every word in my multiple wordlists. You can use this to search (it will give you the same result as `AnagramSets.txt`), or you can make your own list. If you're pulling from .dict files, be sure to remove the semicolon and number score before running this code.
