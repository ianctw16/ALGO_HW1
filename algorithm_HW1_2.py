from nltk.tokenize import RegexpTokenizer

f = open('TheRedandTheBlack.txt', 'r')
b = f.read()

Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)

result = {}
# result_time = []

for i in range(0, len(regeTokened)):
    if(regeTokened[i] not in result):
        result[regeTokened[i]] = 1
    else:
        result[regeTokened[i]] += 1

checknum = 1

for value, key in result.items():
    if(value == checknum):
        print(key)
