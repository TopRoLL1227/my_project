# def is_isogram(string):
#     string = string.lower()
#     seen = set()
#     for letter in string:
#         if letter in seen:
#             return False
#         else:
#             seen.add(letter)
#     return True

# # Test cases
# print(is_isogram("aba"))  # True


def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
        return True




print(is_isogram("aba"))