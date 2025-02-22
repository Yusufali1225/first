                            # 1
# def series_resistance(resistances):
#     total_resistance = sum(resistances)
#     return f"{total_resistance} ohm" if total_resistance == 1 else f"{total_resistance} ohms"
#
# resistances = [1, 5, 6, 3]
# print(series_resistance(resistances))

                            # 2
# def asc_des_none(lst, order):
#     if order == "Asc":
#         return sorted(lst)
#     else:
#         raise ValueError("Invalid order parameter")
# print(asc_des_none([4, 3, 2, 1], "Asc"))  # [1, 2, 3, 4]

                            # 3
# def number_split(n):
#     x = n // 2
#     return [x, n - x]
#
# print(number_split(4))
# print(number_split(10))
# print(number_split(11))
# print(number_split(-9))

                            # 4
# def nam_mer(chords):
#     result = []
#     for chord in chords:
#         if '7' in chord:
#             result.append(chord)
#         else:
#             result.append(chord + '7')
#     return result
# print(nam_mer(["G", "F", "C"]))

                                # 5
# def find_odd(lst):
#     count = {}
#     for num in lst:
#         count[num] = count.get(num, 0) + 1
#     for num, cnt in count.items():
#         if cnt % 2 != 0:
#             return num
#
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
# print(find_odd([10]))
#

                                # 6
# def filter_list(lst):
#     return [item for item in lst if isinstance(item, int)]
#
# print(filter_list([1, 2, "a", "b"]))
# print(filter_list([1, "a", "b", 0, 15]))
# print(filter_list([1, 2, "aasf", "1", "123", 123]))


                                # 7
# first, *middle, last = [1, 2, 3, 4, 5, 6]


                                # 8

# def sumOfCubes(lst):
#     return sum(x**3 for x in lst)
#
# print(sumOfCubes([1, 5, 9]))
# print(sumOfCubes([3, 4, 5]))
# print(sumOfCubes([2]))
# print(sumOfCubes([]))

                                # 9

# def getOnlyEvens(lst):
#     return [x for x in lst if x % 2 == 0]
#
# print(getOnlyEvens([1, 3, 2, 6, 4, 8]))
# print(getOnlyEvens([0, 1, 2, 3, 4]))
# print(getOnlyEvens([1, 2, 3, 4, 5]))


                                # 10

# def sortByLength(lst):
#     return sorted(lst, key=len)
#
# # Misollarni sinab ko'rish
# print(sortByLength(["Google", "Apple", "Microsoft"]))
# print(sortByLength(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# print(sortByLength(["Turing", "Einstein", "Jung"]))
