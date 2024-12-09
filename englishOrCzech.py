import sys
text=''
for line in sys.stdin:
    text+=line.strip()
en_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
           0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
           2.758, 0.978, 2.360, 0.150,  1.974, 0.074]
cz_freq = [8.421, 0.822, 0.740, 3.475, 7.562, 0.084, 0.092, 1.356, 6.073, 1.433,
           2.894, 3.802, 2.446, 6.468, 6.695, 1.906, 0.001, 4.799, 5.212, 5.727,
           2.160, 5.344, 0.016, 0.027, 1.043, 1.503]
def engOrCze(text):
    listOfAlphaFreq=[0] * 26
    engFreq=0
    czeFreq=0
    for alpha in text:
        if not alpha.isalpha():
            continue
        index=ord(alpha.lower()) - ord('a')
        totalLetters = sum(1 for alpha in text if alpha.isalpha())
        listOfAlphaFreq[index]+=1/totalLetters
    for i,freq in enumerate(en_freq):
        engFreq += (listOfAlphaFreq[i]-(freq/100))**2/(freq/100) 
    for i,freq in enumerate(cz_freq):
        czeFreq += (listOfAlphaFreq[i]-(freq/100))**2/(freq/100)
    print(f'Match with English: {engFreq:.2f}')
    print(f'Match with Czech: {czeFreq:.2f}')
    if engFreq>czeFreq: print('Text is in Czech')
    else: print('Text is in English')
engOrCze(text)