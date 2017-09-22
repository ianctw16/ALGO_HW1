from nltk.tokenize import RegexpTokenizer
import time

f = open('TheRedandTheBlack.txt', 'r')
a = 'Eighty-seven miles to go, yet.  Onward!'
b = f.read()

start = time.time()

Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)

tokened_Len = []

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
