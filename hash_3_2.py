# store all data in a signle python list "words"
words=[] 

# read ENG file for data
f=open("words_alpha.txt")
for line in f:
    line=line.rstrip('\n')
    words.append(line)
    print(line)
f.close()

# same word counter variable
counter=0

# read file for data
f=open("kaikkisanat.txt")
for line in f:
    line=line.rstrip('\n')
    # check if word is already in list
    if(line not in words):
        words.append(line)
        print(line)
    # if word exists, do not add, instead +1
    else:
        counter+=1
f.close()

# results
print("Same words",counter)
