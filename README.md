# Anagrams

- I'm Sara and I make [Anagrammies](https://crosshare.org/crosswords/fuVFczCkWWtVXoJdBpRw), puzzles where the answer to the clue anagrams to the filled-in word. I often get comments asking how I am able to do that.
- My method has been to only use a wordlist of anagrams to fill a grid. I used to add to the list manually, putting in anagrams I noticed in the wild. But as the puzzles got bigger, those lists became too small for my purposes, so I wrote a little Python code to do that work for me, and now I wish to share it with you.
- `anagramfind.py` is the program I used to search through my wordlists.
- `allwords.txt` is the list of every word in all of my wordlists. You can use this in the search program if you wish, or make your own list! Be sure to remove the semi colon and score if you're making a list from .dict files.
- I used wordlists from
  * [Peter Broda](https://peterbroda.me/crosswords/wordlist/?fbclid=IwAR04CeR_nhEW5M7CoK6Pyc3lxtzAlD9i9nk6pYadGXWtWN9pTBNWvHCE2hk)
  * [Et Tu, Etui?](https://ettuetui.blogspot.com/2021/07/one-year-of-et-tu-etui.html)
  * [Brooke Husic and Enrique Henestroza Anguiano](https://www.spreadthewordlist.com/wordlist)
  * [The Juggernaut](https://docs.google.com/spreadsheets/d/185Yf0eUsM0CbARllKty5OKFj1Hng2ZzqaLU2p9TN9Ck/edit)
  * [Ricky Cruz](https://docs.google.com/document/d/1XVjHNL6o7Xm8fyNywrkMkL1tuWH8lEN4qyLHQpxYG5E/edit)
  * And myself! But I don't really have a wordlist as much as I add stuff into Crossfire when I think of it.
- `AnagramSets.txt` is the final list of valid anagram sets. You can use this to make your own anagram word list, flesh out an anagram-based theme/clue, or just for light reading idk.
- FAQ
  * Can I make an anagrammy with this?
    - Of course! I'm literally begging for other people to make these puzzles because I want to solve them.
  * Why does the anagrams file look like that?
    - Each line is a list of words/phrases that anagram to each other. Not all of it makes good fill, so it's still necessary to manually look through the list for words you might actually want in your puzzle. I'm still adding to mine and updating its scoring based on how I feel like constructing, so it's best for you to make yours to your own purpose.
  * Does this program take a long time to run? 
    - Yes! I'm a linguist who knows just enough Python to do a task. I don't know much about algorithms or efficiency, the for loop is my best friend.
  * Why are there naughty words in this list?
    - I included words that I scored 0 when I made my `allwords.txt`. Some are marked to 0 because they have no business in puzzles, and some just because I don't like them. It was too much work to sift through my 0's and check which ones I find icky and which ones we should all find icky, so all are included. Apologies for the inevitable filth. 
  * You're so cool, can I follow you on social media?
    - That's very kind of you to say, and [yes you can](https://twitter.com/cantorlope_puz)!
