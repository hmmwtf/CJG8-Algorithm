word = input()
gather = ['a', 'e', 'i', 'o', 'u']

cnt = 0

for i in range(len(word)):
    if word[i] in gather:
        cnt += 1
        
print(cnt)