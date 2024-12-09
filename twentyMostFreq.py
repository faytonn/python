import sys
paragraph = sys.stdin.read()


def is_english_alphabet(char):
    return char in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"


words = []
currentWord = ""

for char in paragraph:
    if is_english_alphabet(char):
        currentWord += char
    else:
        if currentWord != "":
            words.append(currentWord)
            currentWord = ""
                
if currentWord != "":
    words.append(currentWord)
    
wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1


sorted_word_counts = sorted(wordCount.items(), key=lambda item: item[1], reverse=True)
for word, count in sorted_word_counts[:20]:
    print(f"{word} {count}")
        
