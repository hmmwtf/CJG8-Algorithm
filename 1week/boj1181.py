def strcmp(str1, str2):
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

def sort_key(word):
    return (len(word), word)

n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

words = list(set(words))

words.sort(key=sort_key)

for word in words:
    print(word)