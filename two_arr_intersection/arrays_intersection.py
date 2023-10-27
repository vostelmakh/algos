# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть [1, 2, 2, 3] (порядок неважен)

def arrays_intersection(arr1, arr2):
    first_arr_dict = {}

    for i in arr1:
        if i in first_arr_dict:
            first_arr_dict[i] = first_arr_dict.get(i) + 1
        else:
            first_arr_dict[i] = 1

    common_elements = []

    for i in arr2:
        if i in first_arr_dict:
            common_elements.append(i)

            if first_arr_dict.get(i) == 1:
                del first_arr_dict[i]
            else:
                first_arr_dict[i] = first_arr_dict.get(i) - 1

    return common_elements