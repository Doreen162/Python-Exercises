# my lists of numbers
num = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
print(sum(num))
num.sort()
print(num)


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


duplicate = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
print(Remove(duplicate))