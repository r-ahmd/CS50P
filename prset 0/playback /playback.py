a = input()
a = a.split()
for word in a:
    word_index=a.index(word)
    if word_index % 2 ==0:
        a.insert(word_index+1, '...')
a.pop()
for word in a:
    print(word, end="")
print("")
