"""Pig Latin"""
words = input("Enter some text to translate to pig latin")
print("You have entered: {}".format(words))


words = words.split(' ')

for i in words:
    if len(i) >= 3:
        i = i + "{}ay".format(i[0])
        i = i[1:]
        print(i)
    else:
        pass
 