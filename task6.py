# 1

# lst = [30, 75, 9, 97, 50, -4, 70, 59]
#
# largest_number = max(lst)
# print("Largest number:", largest_number)
#
# smallest_number = min(lst)
# lst.remove(smallest_number)
# print("Smallest number removed:", smallest_number)
#
# lst.sort()
# print("List in ascending order:", lst)
#
# last_4_numbers = lst[-4:]
# print("Last 4 numbers:", last_4_numbers)


# 2

# main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
#
# count = 0
#
# for sublist in main_lst:
#     if isinstance(sublist, list) and len(sublist) == 2 and sublist[0] == "python":
#         count += 1
#
# print(count)


# 3

# my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
#
# sentence = ' '.join(word.capitalize() for word in my_lst)
#
# print(sentence)


# 4

# my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
#
# copied_lst = []
#
# for item in my_lst:
#     if isinstance(item, list):
#         copied_lst.append(item[:])
#     else:
#         copied_lst.append(item)
#
# print(copied_lst)


# 5

# my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
#
# my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
#
# print(my_lst)


# 6

# nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
#
# total_sum = sum(nums)
#
# print(total_sum)


# 7

# tuple1 = (4, 'python', 'GSG', [8, 3, 1])
#
# tuple2 = tuple1 + (9,)
#
# print(tuple2)


# 8

# tuple1 = (4, 'python', 'GSG', [8, 3, 1])
# tuple2 = ('Java', 'C++', 7.8)
#
# new_tuple = tuple1 + tuple2
#
# print(new_tuple)
