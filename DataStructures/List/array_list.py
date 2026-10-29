def new_list():
    newlist = {
        "elements": [],
        "size": 0,
        "first": None,
        "last": None,
    }
    return newlist

def get_element(my_list, index):
    if index < 0 or index >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]  
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1 

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1 
    return my_list 

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def last_element(my_list):
    if not my_list:
        return None
    return my_list[-1] 
    
def is_empty(my_list):
    return my_list["size"] == 0

def first_element(my_list):
    if not my_list:
        return None
    return my_list["elements"][0]


def insert_element(my_list, element, index):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list,index, element):
    my_list["elements"][index] = element
    if index < 0 or index >= my_list["size"]:
        raise IndexError("list index out of range")
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise IndexError("list index out of range")
    temp = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = temp
    return my_list

def delete_element(my_list, index):
    if index < 0 or index >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].pop(index)
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    my_list["size"] -= 1
    return my_list["elements"].pop(0)

def size(my_list):
    return my_list["size"]

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    my_list["size"] -= 1
    return  my_list["elements"].pop()

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"] or num_elements < 0 or pos_i + num_elements > my_list["size"]:
        raise IndexError("list index out of range")
    sublist = new_list()
    for i in range(pos_i, pos_i + num_elements):
        add_last(sublist, my_list["elements"][i])
    return sublist
def shell_sort (my_list, sort_crit):
    size1 = size(my_list)
    gap = size1 // 2
    while gap > 0:
        pos1 = gap
        while pos1 < size1:
            pos2 = pos1
            while pos2 >= gap and sort_crit(get_element(my_list, pos2), get_element(my_list, pos2 - gap)):
                exchange(my_list, pos2, pos2 - gap)
                pos2 -= gap
            pos1 += 1
        gap = gap // 2
    return my_list
def selection_sort(my_list, sort_crit):
    size1 = size(my_list)
    pos1 = 0

    while pos1 < size1:
        minimum = pos1
        pos2 = pos1 + 1

        while pos2 < size1:
            if sort_crit(get_element(my_list, pos2), get_element(my_list, minimum)):
                minimum = pos2
            pos2 += 1

        exchange(my_list, pos1, minimum)
        pos1 += 1

    return my_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def insertion_sort(my_list, sort_crit):
    if sort_crit is None:
        sort_crit = default_sort_criteria
    size1 = size(my_list)
    pos1 = 1
    while pos1 < size1:
        pos2 = pos1
        while (pos2 > 0) and (sort_crit(get_element(my_list, pos2),
            get_element(my_list, pos2-1))):
            exchange(my_list, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return my_list
def merge_sort(my_list, sort_crit):
    size1 = size(my_list)
    if size1 <= 1:
        return my_list
    else:
        mid = size1 // 2
        left = sub_list(my_list, 0, mid)
        right = sub_list(my_list, mid, size1 - mid)
        left = merge_sort(left, sort_crit)
        right = merge_sort(right, sort_crit)

        merged_list = new_list()
        left_size = size(left)
        right_size = size(right)
        left_index = 0
        right_index = 0

        while left_index < left_size and right_index < right_size:
            if sort_crit(get_element(left, left_index), get_element(right, right_index)):
                add_last(merged_list, get_element(left, left_index))
                left_index += 1
            else:
                add_last(merged_list, get_element(right, right_index))
                right_index += 1

        while left_index < left_size:
            add_last(merged_list, get_element(left, left_index))
            left_index += 1

        while right_index < right_size:
            add_last(merged_list, get_element(right, right_index))
            right_index += 1

    return merged_list

def partition(my_list, low, high, sort_crit):
    pivot = get_element(my_list, high)
    smaller_index = low - 1

    for current in range(low, high):
        if sort_crit(get_element(my_list, current), pivot):
            smaller_index += 1
            exchange(my_list, smaller_index, current)

    exchange(my_list, smaller_index + 1, high)
    return smaller_index + 1

def quick_sort_recursive(my_list, low, high, sort_crit):
    if low < high:
        pivot_pos = partition(my_list, low, high, sort_crit)
        quick_sort_recursive(my_list, low, pivot_pos - 1, sort_crit)
        quick_sort_recursive(my_list, pivot_pos + 1, high, sort_crit)

def quick_sort(my_list, sort_crit):
    quick_sort_recursive(my_list, 0, size(my_list) - 1, sort_crit)
    return my_list