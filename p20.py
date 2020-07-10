# import random
# import string
#
# letters = string.ascii_letters
# digits = string.digits
# punctuation = string.punctuation
#
# sequence = '{}{}{}'.format(letters,digits,punctuation)
# sequence = str(sequence)
#
#
# password = ''.join(random.sample(sequence, int(input("Enter the length of the password you want ? : "))))
# print(password)

import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

sequence = "{}{}{}".format(letters, digits, punctuation)
sequence = str(sequence)

password = ''.join(random.sample(sequence, int(input("Enter the length of the password you want ? :"))))
print(password)
