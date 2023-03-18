pt = input("Enter the text: ")
key = input("Enter the 26 length key: ")
ept = []
endict = {}

for i in range(26):
    if(key[i].isupper()):
        endict[chr(65+i)] = key[i]
        endict[chr(97+i)] = key[i].lower()
    else:
        endict[chr(97+i)] = key[i]
        endict[chr(65+i)] = key[i].upper()

for i in pt:
    if(i.isupper() or i.islower()):
        ept.append(endict[i])
    else:
        ept.append(i)
    
ept = ''.join(ept)
print(ept)

enpt = input("Enter the encrpted string: ")
encripted_key = input("Enter encripted key: ")
dpt = []
dedict = {}
for i in range(26):
    if(key[i].isupper()):
        dedict[key[i]] = chr(65+i)
        dedict[key[i].lower()] = chr(97+i)
    else:
        dedict[key[i]] = chr(97+i)
        dedict[key[i].upper()] = chr(65+i)

for i in enpt:
    if(i.isupper() or i.islower()):
        dpt.append(dedict[i])
    else:
        dpt.append(i)
        
dpt = ''.join(dpt)
print(dpt)
    

