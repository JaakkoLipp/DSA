words=[]
f=open("words_alpha.txt")
for line in f:
    line=line.rstrip('\n')
    words.append(line)
    print(line)
f.close()

counter=0

f=open("kaikkisanat.txt")
for line in f:
    line=line.rstrip('\n')
    if(line not in words):
        words.append(line)
        print(line)
    else:
        counter+=1
f.close()
print("Same words",counter)
