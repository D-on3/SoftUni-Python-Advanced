# def vowel_filter(func):
#     VOWELS = "aoueiy"
#     def wrapper():
#         result = func()
#         return [x for x in result if x in VOWELS]
#     return wrapper

from functools import wraps


def vowel_filter(func):
    vowels = "aoueiy"

    @wraps(func)
    def wrapper():
        result = func()
        return [x for x in result if x.lower() in vowels]

    return wrapper



@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
