# frequency = {}
# text = input()
# for i in text:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
#
# print("{} -> {}".format(text, str(frequency)))
#

frequency = {}
char = input()
for i in char:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("{} -> {}".format(char, frequency))

