# def isBalanced(str):
#     count = 0
#     for i in str:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0
#
#
# string = input()
# print(isBalanced(string))


# def is_balanced(str):
#     count = 0
#     for i in str:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0
#
#
# string = input()
# print(is_balanced(string))


"""To check if parenthesis are balanced in a string with characters"""


def is_balanced(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    return count == 0


str = input()
print(is_balanced(str))
