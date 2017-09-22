from nltk.tokenize import RegexpTokenizer

f = open('TheRedandTheBlack.txt', 'r')
a = 'I I You i u you'
b = f.read()

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


checknum = 1
control = 0

for key, value in result.items():
    # print(key)
    if(value == checknum):
        print(key, end="    ")
        control = 1
