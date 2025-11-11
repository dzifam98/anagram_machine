# You select a number and insert different words.
# The program outputs a dictionary values in which the words grouped in it are anagrams (contain the same letters).
def select_listamount():
    try:
        number = int(input("How many words do you want in your word list? "))
        return number
    except ValueError:
        print("Not an integer, try again.")
        newnumber = select_listamount()
        return newnumber
    
def make_wordlist():
    wordlist = []
    for t in range(select_listamount()):
        word = input("Enter a word: ")
        if word not in wordlist:
            wordlist.append(word)
            print(f"{word}: {t+1} words added.")
        else:
            while word in wordlist:
                print(f'{word} is already in the list. Try another one.')
                word = input("Enter a word: ")
            wordlist.append(word)
            print(f"{word}: {t+1} words added.")
    print("Finished.")
    return wordlist
    
def anagrammer(listy):
    worddict = {}
    sortwords = [''.join(sorted(i.lower())) for i in listy]
    #sorted word obtained by https://datagy.io/python-sort-string/
    for i in sortwords:
        if sortwords.count(i) > 1:
            worddict[sortwords.index(i)] = [n for n in listy if ''.join(sorted(n.lower())) == i]
            #the key of each dictionary entry does not matter, because only the values (list comp) matters. 
    print(worddict.values())
                
if __name__ == "__main__":
    words_here = make_wordlist()
    anagrammer(words_here)