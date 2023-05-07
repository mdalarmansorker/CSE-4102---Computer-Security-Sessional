#shift cipher
def encryption(text, key):
    ent = []
    a = ''
    for l in text:
        if(l.isupper()):
            a = chr((ord(l) + key-65) % 26+65)
        elif(l.islower()):
            a = chr((ord(l) + key - 97) % 26 + 97)
        else:
            a = l

        ent.append(a)

    ent = ''.join(ent)
    return ent


def decryption(text, key):
    dec = []
    a = ''
    for l in text:
        if (l.isupper()):
            a = chr((ord(l) - key - 65) % 26 + 65)
        elif (l.islower()):
            a = chr((ord(l) - key - 97) % 26 + 97)
        else:
            a = l

        dec.append(a)

    dec = ''.join(dec)
    return dec

print("Encryption: ")
key = int(input("Key: "))
text = input("Plain text: ")
print(encryption(text, key))

print("Decryption: ")
key2 = int(input("Key: "))
text2 = input("Plain text: ")
print(decryption(text2, key2))



