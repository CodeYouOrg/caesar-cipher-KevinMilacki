# add your code here


def cipher(text):
    result = ""
    
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) + 5 - 65) % 26 + 65)
            result += new_char
        elif char.islower():
            new_char = chr((ord(char) + 5 - 97) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

text = input("What do you want to encode?:")

print(cipher(text))

