from nltk.tokenize import RegexpTokenizer
import time


# open txt file.
print()
print('1: Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt')
print('2: Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt')
# print('3: The_Citadel-A_J_Cronin-Total words 36702-Unique words 2556.txt')
print('4: The_Old_Man_and_the_Sea-Ernest_Hemingway-Total words 12759-Unique words 1203.txt')
print('5: Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt')
print()
opt_input = input('Choose a book(Enter the number):')
if(opt_input == '1'):
    f = open('Crime_and_Punishment_Fyodor_Dostoyevsky-Total words 34004-Unique words 3331.txt', 'r')
elif(opt_input == '2'):
    f = open('Forrest_Gump-John_Escott-Total words 9095-Unique words 1012.txt', 'r')
# elif(opt_input == '3'):
    # f = open('The_Citadel_A_J_Cronin_Total_words_36702_Unique_words_2556.txt', 'r')
elif(opt_input == '4'):
    f = open('The_Old_Man_and_the_Sea-Ernest_Hemingway-Total words 12759-Unique words 1203.txt', 'r')
elif(opt_input == '5'):
    f = open('Spider-man-Stan_Lee-Total words 4342-Unique words 514.txt', 'r')
print()
b = f.read()


# let output print in order
def printStoreKey(store_key):
    while(len(store_key) != 0):
        try:
            print(min(store_key), end='     ')
            store_key.remove(min(store_key))
        except:
            pass


# start counting execution time
start = time.time()

# start counting execution time
Regetokenizer = RegexpTokenizer(r'\w+')
regeTokened = Regetokenizer.tokenize(b)
f.close()
regeTokened = list(map(str, regeTokened))

# let all words be low case.
for i in range(0, len(regeTokened)):
    regeTokened[i] = regeTokened[i].lower()

# check list's characters are all in ascII 97~122
i = 0
while(i != len(regeTokened)):
        if(ord(regeTokened[i][0]) not in range(97, 122)):
            regeTokened.remove(regeTokened[i])
            i = i - 1
        i = i + 1

result = {}

# sotre all words in dictionary and count its frequences.
for i in range(0, len(regeTokened)):
    if(regeTokened[i] not in result):
        result[regeTokened[i]] = 1
    else:
        result[regeTokened[i]] += 1

biggest = 0

# find the bigget word frequence in dictionary.
for key, value in result.items():
    if(value > biggest):
        biggest = value

# print(biggest)

checknum = biggest
store_key = []

# main part. start in biggest word in dictionary and decrease to find other word
while(checknum >= 1):
    store_key = []
    print(checknum, ':', end=' ')
    for key, value in result.items():
        if(value == checknum):
            # print(key, end='    ')
            store_key.append(key)
    printStoreKey(store_key)
    print()
    checknum -= 1

# print result
print("******************************************************************")
print('Program total execution time:', end=' ')
result_time = time.time() - start
print(result_time)
print("******************************************************************")

# save result in txt file
checknum = biggest
s = open('OUTPUT-B.txt', 'w')
s.write('Program total execution time: ')
s.write(str(result_time))
s.write('\n\n******************************************************************\n\n')
while(checknum >= 1):
    s.write(str(checknum))
    s.write(':')
    for key, value in result.items():
        if(value == checknum):
            s.write(str(key))
            s.write(' ')
    s.write('\n')
    checknum -= 1
s.close()
