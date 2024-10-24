import sys

before,after = 10, 10
output = ''
letterToNumber = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
    'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25,
    'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
    'y': 34, 'z': 35
}

for line in sys.stdin:
    line = line.strip()
    result = ''
    
    if '>' in line:
        before, after = line.split('>')
        continue
    else:
        base10ConvertedInt = 0
        length = len(line)
        
        for index in line:
            if index.isalpha():
                index = letterToNumber[index.lower()]
            base10ConvertedInt += int(index) * (int(before) ** (length - 1))
            length -= 1
            
        if int(after) != 10:
            while base10ConvertedInt > 0:
                remainder = base10ConvertedInt % int(after)
                if remainder > 9:
                    remainder = chr(remainder - 10 + ord('a'))
                result = str(remainder) + result
                base10ConvertedInt //= int(after)
            if result == '':
                result = '0'
            output += result + '\n'
        else:
            result += str(base10ConvertedInt)
            output += result + '\n'
            
print(output)