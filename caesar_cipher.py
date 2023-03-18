def encriptions():
    key = int(input("Key = "))
    text = input("Text = ")
    entext = ""
    for letter in text:
        if(letter == " "):
            entext += letter
            continue
        elif(letter.islower()):
            if((ord(letter)+key) > 122):
                entext += chr((ord(letter)+key)-122 + 96)
            else:
                entext += chr(ord(letter)+key)
        elif(letter.isupper()):
            if((ord(letter)+key) > 90):
                entext += chr((ord(letter)+key)-90 + 64)
            else:
                entext += chr(ord(letter)+key)
        elif(letter.isdigit()):
            entext += letter
            continue
        else:
            entext += letter
       
    text = entext
    print("Encripted text: " + text)

def decriptions():
    key = int(input("Key = "))
    text = input("Text = ")
    detext = ""
    for letter in text:
        if(letter == " "):
            detext += letter
            continue
        elif(letter.islower()):
            if((ord(letter)-key) < 97):
                detext += chr(123 - (97 - (ord(letter)-key)))
            else:
                detext += chr(ord(letter)-key)
        elif(letter.isupper()):
            if((ord(letter)+key) < 65):
                detext += chr(91 - (65 - (ord(letter)-key)))
            else:
                detext += chr(ord(letter)-key)
        elif(letter.isdigit()):
            detext += letter
            continue
        else:
            detext += letter
    text = detext
    print("Decripted Text: " + text)

encriptions()
decriptions()