from nltk.tokenize import RegexpTokenizer
import time

# f = open('TheRedandTheBlack.txt', 'r')
# f = open('Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt', 'r')
# f = open('Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt')
f = open('Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt')
a = 'Eighty-seven miles to go, yet.  Onward!'
b = f.read()

start = time.time()

Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)

score = 0

for i in range(0, len(regeTokened)):
    regeTokened[i] = regeTokened[i].lower()

print(regeTokened)

for i in range(0, len(regeTokened)):
    j = i + 1
    print(ord(regeTokened[i][0]))
    while(j < len(regeTokened)):
        if(ord(regeTokened[i][0]) > ord(regeTokened[j][0])):
            score = score + 1
        j = j + 1

print(time.time() - start)
print("******************************************************************")
print(score)
"""
for word in regeTokened:
    # print(word, len(word))
    tokened_Len.append(len(word))
     # tokened_Len.append(len(word))
     # print(j)
     # j = j + 1

# print(tokened_Len)
# print(len(tokened_Len))

score = []
tmp = 0

for i in range(0, len(tokened_Len)):
    j = i + 1
    tmp = 0
    while(j < len(tokened_Len)):
        if(tokened_Len[j] > tokened_Len[i]):
            tmp = tmp + 1
            j = j + 1
        else:
            j = j + 1
    score.append(tmp)

print(time.time() - start)
print("******************************************************************")
print(score)
# print(len(score))
"""
