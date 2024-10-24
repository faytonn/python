def ceasarCipher(shift, message):
    shift = shift % 26  #(index ile) 0 ve 25  arasi olmalidi valuelarin shifti cunki 26 herf var
    encryptedMessage = ""
    
    for char in message:
        if 'a' <= char <= 'z': #eger lowercasedise
            cipheredChar = chr((ord(char) - ord('a') + shift) % 26 + ord('A'))
            encryptedMessage += cipheredChar
        elif 'A' <= char <= 'Z': #eger uppercasedise
            cipheredChar = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encryptedMessage += cipheredChar
        else:
            encryptedMessage += char
            
    return encryptedMessage

k = int(input())
text = input()

result = ceasarCipher(k, text)
print(result)