from nltk.tokenize import RegexpTokenizer
import time

# open txt file.
print()
print('1: Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt')
print('2: Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt')
print('3: The_Citadel-A_J_Cronin-Total words 36702-Unique words 2556.txt')
print('4: The_Old_Man_and_the_Sea-Ernest_Hemingway-Total words 12759-Unique words 1203.txt')
print('5: Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt')
print()
opt_input = input('Choose a book(Enter the number):')
if(opt_input == '1'):
    f = open('Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt', 'r')
elif(opt_input == '2'):
    f = open('Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt', 'r')
elif(opt_input == '3'):
    f = open('The_Citadel_A_J_Cronin_Total_words_36702_Unique_words_2556.txt', 'r')
elif(opt_input == '4'):
    f = open('The_Old_Man_and_the_Sea-Ernest_Hemingway-Total words 12759-Unique words 1203.txt', 'r')
elif(opt_input == '5'):
    f = open('Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt', 'r')
print()
b = f.read()

# start counting execution time
start = time.time()

# separate words and store in list
Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)
f.close()
regeTokened = list(map(str, regeTokened))

score = 0

# let all words be low case.
for i in range(0, len(regeTokened)):
    regeTokened[i] = regeTokened[i].lower()

# print(len(regeTokened))
# check list's characters are all in ascII 97~122
i = 0
while(i != len(regeTokened)):
        if(ord(regeTokened[i][0]) not in range(97, 122)):
            regeTokened.remove(regeTokened[i])
            i = i - 1
        i = i + 1

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
print('Entropy: ', score)

# save result in txt file
s = open('OUTPUT-A.txt', 'w')
s.write('Program total execution time: ')
s.write(str(result_time))
s.write('\n\n******************************************************************\n\n')
s.write('Entropy: ')
s.write(str(score))
s.close()
