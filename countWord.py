text = str(input('Paste some text: \n'))

wordlist = {}
spltxt = text.split(' ')
for word in spltxt:
    word = word.lower()
    if word not in wordlist:
        wordlist[word] = 1
    else:
        wordlist[word] += 1
print(wordlist)