name=input("enter a name")
vowel="aeiou"
for i in range(0,len(vowel)):
    for j in range(0,len(name)):
        if vowel[i]==name[j]:
            print(name[j]) 
for i in range(0,len(name)):
    result = ''.join(sorted(name))
    if result[i] not in vowel:
        print(result[i])

        
