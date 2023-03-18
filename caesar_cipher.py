def encriptions():
    key = int(input("Key = "))
    text = input("Text = ")
    entext = ""
    for letter in text:
        if(letter.islower()):
            entext += chr((ord(letter)+key-97)%26+97)
        elif(letter.isupper()):
            entext += chr((ord(letter)+key-65)%26+65)
        else:
            entext += letter
       
    text = entext
    print("Encripted text: " + text)

def decriptions():
    key = int(input("Key = "))
    text = input("Text = ")
    detext = ""
    for letter in text:
        if(letter.islower()):
            detext += chr((ord(letter)-key-97)%26+97)
        elif(letter.isupper()):
            detext += chr((ord(letter)-key-65)%26+65)
        else:
            detext += letter
    text = detext
    print("Decripted Text: " + text)

encriptions()
decriptions()