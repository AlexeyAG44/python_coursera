# Дан текст.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# 1 способ
inputFile = open('input.txt')
myDict = {}
for word in inputFile.read().split():
    myDict[word] = myDict.get(word, 0) + 1
myList = sorted(myDict.items())
myList.sort(key=lambda x: x[1], reverse=True)
print(myList[0][0])

# 2 способ

file = open('input.txt')
words = {}
n = []
for line in file:
    n.extend(line.split())
for i in n:
    words[i] = words.get(i, 0) + 1
a = max(sorted([i for i, k in words.items()]), key=lambda x: words[x])  # не до конца разобрался с этаким выводом
print(a)
