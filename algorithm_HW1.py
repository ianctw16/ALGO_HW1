from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
import time

f = open('TheRedandTheBlack.txt', 'r')
a = 'Eighty-seven miles to go, yet.  Onward!'
b = f.read()

tokenizer = TreebankWordTokenizer()
Regetokenizer = RegexpTokenizer(r'\w+')

sent_tokenize_list =sent_tokenize(b)
# print(tokenizer.tokenize(b))
tokened = tokenizer.tokenize(b)
regeTokened = Regetokenizer.tokenize(b)

# print(tokened[0])
# print(regeTokened)

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

start = time.time()

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
