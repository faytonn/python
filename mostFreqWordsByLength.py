import sys 


def isLetter(char):
    lowercaseLetters = 'qwertyuiopasdfghjklzxcvbnm'
    capitalLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    return char in lowercaseLetters or char in capitalLetters

def main():
    text = sys.stdin.read()
    
    words = []
    currentWord = ""
    
    for char in text:
        if isLetter(char):
            currentWord += char
        else:
            if currentWord:
                words.append(currentWord.lower())
                currentWord = ""
                
    if currentWord:
        words.append(currentWord.lower())
        
    countByLen = {}
    
    for w in words:
        length = len(w)
        if length not in countByLen:
            countByLen[length] = {}
        if w not in countByLen[length]:
            countByLen[length][w] = 0
        countByLen[length][w] += 1
        
    for length in sorted(countByLen.keys()):
        wordDictionary = countByLen[length]
        
        maxFrequency = 0
        for word, count in wordDictionary.items():
            if count > maxFrequency:
                maxFrequency = count
                
        mostFrequentWords = []
        for word, count in wordDictionary.items():
            if count == maxFrequency:
                mostFrequentWords.append(word)
                
        mostFrequentWords.sort()
        
        if maxFrequency == 1:
            occurrenceWord = "occurrence"
        else:
            occurrenceWord = "occurrences"
        
        wordsStr = " ".join(mostFrequentWords)
        
        print(f"length {length}: {wordsStr} ({maxFrequency} {occurrenceWord})")
        
if __name__ == "__main__":
    main()
            




