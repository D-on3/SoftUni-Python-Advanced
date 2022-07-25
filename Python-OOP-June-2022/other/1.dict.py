messed_dict = {"1": 2, "2": 4, "3": 6, "4": 10}
prices = [1, 2]
coef = 3.2
# UPDATED PRICE

for key, val in messed_dict.items():

    if int(key) in prices:
        val *= coef
        print(f"{key}-{val}")

print(messed_dict)
# messed_dict = {"1": 2, "2": 4, "3": 6, "4": 10}
# prices = [1, 2]
# coef = 3.2
# # UPDATED PRICE
# for key, val in messed_dict.items():
#
#     if int(key) in prices:
#         val *= coef
#         print(f"{key}-{val}")
