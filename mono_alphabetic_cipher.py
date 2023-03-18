pt = input("Enter the text: ")
ept = []
key = input("Enter the 26 length key: ")

endict = {}
dedict = {}

for i in range(26):
    if(key[i].isupper()):
        endict[chr(65+i)] = key[i]
        dedict[key[i]] = chr(65+i)
        endict[chr(97+i)] = key[i].lower()
        dedict[key[i].lower()] = chr(97+i)
    else:
        endict[chr(97+i)] = key[i]
        dedict[key[i]] = chr(97+i)
        endict[chr(65+i)] = key[i].upper()
        dedict[key[i].upper()] = chr(65+i)

for i in pt:
    if(i.isupper() or i.islower()):
        ept.append(endict[i])
    else:
        ept.append(i)
    
ept = ''.join(ept)
print(ept)

enpt = input("Enter the encrpted string: ")
# encripted_key = input("Enter encripted key: ")
# print(dedict['z'])
dpt = []
for i in enpt:
    if(i.isupper() or i.islower()):
        dpt.append(dedict[i])
    else:
        dpt.append(i)
dpt = ''.join(dpt)
print(dpt)
    

