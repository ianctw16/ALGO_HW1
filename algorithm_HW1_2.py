from nltk.tokenize import RegexpTokenizer
import time

# f = open('TheRedandTheBlack.txt', 'r')
f = open('Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt', 'r')
a = 'I I You i u you'
b = f.read()

start = time.time()

Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)

for i in range(0, len(regeTokened)):
    regeTokened[i] = regeTokened[i].lower()

result = {}
# result_time = []

for i in range(0, len(regeTokened)):
    if(regeTokened[i] not in result):
        result[regeTokened[i]] = 1
    else:
        result[regeTokened[i]] += 1

biggest = 0

for key, value in result.items():
    if(value > biggest):
        biggest = value

# print(biggest)

checknum = biggest

while(checknum >= 1):
    print(checknum, ':', end=' ')
    for key, value in result.items():
        if(value == checknum):
            print(key, end='    ')
    print()
    checknum -= 1

print(time.time() - start)
print("******************************************************************")
