def occurences(text):
    frequency = {}
    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print("{} -> {}".format(text, str(frequency)))


occurences(input())

