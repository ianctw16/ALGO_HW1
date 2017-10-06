from nltk.tokenize import RegexpTokenizer
import time

# open txt file.
# f = open('TheRedandTheBlack.txt', 'r')
# f = open('Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt', 'r')
# f = open('Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt', 'r')
# f = open('The_Citadel-A_J_Cronin-Total words 36702-Unique words 2556.txt', 'r')
# f = open('The_Old_Man_and_the_Sea-Ernest_Hemingway-Total words 12759-Unique words 1203.txt', 'r')
f = open('Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt', 'r')
a = 'Eighty-seven miles to go, yet.  Onward!'
b = f.read()

# start counting execution time
start = time.time()

# separate words and store in list
Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)

score = 0

# let all words be low case.
for i in range(0, len(regeTokened)):
    regeTokened[i] = regeTokened[i].lower()

# print(len(regeTokened))
# check charactor not in ascII 97~122
for i in range(0, len(regeTokened)):
    try:
        if(ord(regeTokened[i][0]) not in range(97, 122)):
            regeTokened.remove(regeTokened[i])
    except:
        pass

# print(len(regeTokened))

# main part. start in first word and check the rest which one's ascII is small than it.
for i in range(0, len(regeTokened)):
    j = i + 1
    # print(ord(regeTokened[i][0]))
    while(j < len(regeTokened)):
        if(ord(regeTokened[i][0]) > ord(regeTokened[j][0])):
            score = score + 1
        elif(ord(regeTokened[i][0]) == ord(regeTokened[j][0])):
            try:
                if(ord(regeTokened[i][1]) > ord(regeTokened[j][1])):
                    score = score + 1
                elif(ord(regeTokened[i][1]) == ord(regeTokened[j][1])):
                    try:
                        if(ord(regeTokened[i][2]) > ord(regeTokened[j][2])):
                            score = score + 1
                    except:
                        pass
            except:
                pass
        j = j + 1

# print result
print("******************************************************************")
print('Program total execution time:', end=' ')
result_time = time.time() - start
print(result_time)
print("******************************************************************")
print(score)

# save result in txt file
s = open('OUTPUT-A.txt', 'w')
s.write('Program total execution time: ')
s.write(str(result_time))
s.write('\n\n******************************************************************\n\n')
s.write(str(score))
s.close()
