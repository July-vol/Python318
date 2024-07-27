# Вычислить количество отрицательных чисел в массив:[-2, 3, 8, -11, -4, 6]
# n = 3


def count(lst):
    if len(lst) == 1:
        if lst[0] < 1:
            return 1
        else:
            return 0
    else:
        if lst[0] > 1:
            return count(lst[1:])
        else:
            return 1 + count(lst[1:])


print("n = ", count([-2, 3, 8, -11, -4, 6]))
