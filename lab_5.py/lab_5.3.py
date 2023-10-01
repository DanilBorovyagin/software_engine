def rep(input_list):
    mem = input_list[1]
    input_list[1] = input_list[3]
    input_list[3] = mem

    return input_list


print(rep([5,4,3,2,1]))


def swap(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(swap([1,2,3,4,5]))
