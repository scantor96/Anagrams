# Anagrams

- I make Anagrammies, puzzles entirely populated with valid anagrams and I often get comments wondering how I am able to do that.
- My method has been to only use a wordlist of anagrams to fill a grid. I used to add to the list manually, putting in anagrams I noticed in the wild. But as the puzzles got bigger, those lists became too small for my purposes, so I wrote a little Python code to do that work for me.
- I use a lot of different wordlists when I make puzzles, I've linked to some of the larger ones below. I've attached the code I used to find valid pairs. 
- I've uploaded `allwords.txt`, which is the list of every word in my multiple wordlists. You can use this to search (it will give you the same result as `AnagramSets.txt`), or you can make your own list. If you're pulling from .dict files, be sure to remove the semicolon and number score before running this code.
- FAQ
  * Can I also make an anagrammy with this list/code?
    - Of course! I'm literally begging for someone else to make one of these puzzles because I want to solve one.
  * Why does the text file look like that?
    - Each line is a list of words that anagram to each other. Not all of it makes good fill, so it's still necessary to look through the list for words you might actually want in your puzzle, and create a .dict file of those good words.
  * Did this program take a long time to run? 
    - Yes! I'm a linguist who knows just enough Python to do a task. I don't know much about algorithms or efficiency, the for loop is my best friend.
  * Why are there naughty words in this list?
    - I included words that I scored 0 when I made my `allwords.txt`. Some are marked to 0 because they have no business in puzzles, and some just because I don't like them. It was too much work to sift through my 0's and check which ones I find icky and which ones we should all find icky, so all are included. Apologies for the inevitable filth. 
