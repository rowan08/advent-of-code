with open('input.txt') as f:
    data = list(sorted(map(int, f.readlines())))


def get_2_values(numbers_list):

    for i in reversed(numbers_list):
        for k in numbers_list:
            if i + k == 2020:
                return i, k
            elif i + k > 2020:
                break

    return None, None


def get_3_values(numbers_list):

    for index_1, value_1 in enumerate(numbers_list):

        index_2 = index_1 + 1
        for value_2 in numbers_list[index_2:]:

            index_3 = index_2 + 1
            for value_3 in numbers_list[index_3:]:

                total = sum([value_1, value_2, value_3])
                if total == 2020:
                    return value_1, value_2, value_3
                elif total > 2020:
                    break

    return None, None, None


if __name__ == '__main__':

    print('\ngetting 2 values:')
    value_1, value_2 = get_2_values(data)
    if value_1:
        print(value_1, value_2, value_1 * value_2)

    print('\ngetting 3 values:')
    value_1, value_2, value_3 = get_3_values(data)
    if value_1:
        print(value_1, value_2, value_3, value_1 * value_2 * value_3)

    print('\ncomplete\n')
