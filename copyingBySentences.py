import sys

def process_input():
    input_text = sys.stdin.read()
    sentences = []
    current_sentence = []
    
    for char in input_text:
        if char == '.':
            current_sentence.append(char)
            sentences.append(''.join(current_sentence).strip())
            current_sentence = []
        elif char == '\n':
            current_sentence.append(' ')
        else:
            current_sentence.append(char)
    
    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    process_input()