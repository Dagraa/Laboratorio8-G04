def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]

    while searchpos < pos:
        node = node["next"]
        searchpos += 1

    return node["info"]
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0

    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1

    return count

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if is_empty(my_list):
        return None

    first_node = my_list["first"]
    element = my_list["first"]["info"]

    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1

    if is_empty(my_list):
        my_list["last"] = None 

    return element


def remove_last(my_list):
    if is_empty(my_list):
        return None
    
    if size(my_list) == 1:
        return remove_first(my_list)

    current = my_list["first"]
    while current["next"]["next"] is not None:
        current = current["next"]
    element = my_list["last"]["info"]

    current["next"] = None
    my_list["last"] = current
    my_list["size"] -= 1

    return element

def delete_element(my_list, pos):
    if pos < 1 or pos > size(my_list):
        return my_list

    if pos == 1:
        remove_first(my_list)
        return my_list

    current = my_list["first"]
    for _ in range(1, pos - 1):
        current = my_list.get_next(current)

    node_to_delete = my_list.get_next(current)
    current["next"] = my_list.get_next(node_to_delete)

    if pos == size(my_list):
        my_list["last"] = current
    my_list["size"] -= 1

    return my_list

def add_first(my_list, element):
    new_node = {
        "info": element,
        "next": my_list["first"]
    }
    my_list["first"] = new_node
    if my_list["size"] == 0:
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list
def size(my_list):
    return my_list["size"]
def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["first"]["info"]
    return None
def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["last"]["info"]
    return None
def add_last(my_list, element):
    new_node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos == 0: 
        add_first(my_list, element)
    elif pos == size(my_list):
        add_last(my_list, element)
    else:
        current = my_list["first"]
        for i in range(pos - 1):
            current = current["next"]
        new_node = {
            "info": element,
            "next": current["next"]
        }
        current["next"] = new_node
        my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos<0 or pos>=my_list["size"]:
        raise Exception('IndexError: list index out of range')
    current = my_list["first"]
    for i in range(pos):
        current = current["next"]
    current["info"] = new_info 
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    if pos_1 == pos_2:
        return my_list
    current_1 = my_list["first"]
    for i in range(pos_1):
        current_1 = current_1["next"]
    current_2 = my_list["first"]
    for i in range(pos_2):
        current_2 = current_2["next"]
    current_1["info"], current_2["info"] = current_2["info"], current_1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"] or num_elements < 0 or pos + num_elements > my_list["size"]:
        raise Exception('IndexError: list index out of range')
    sublist = new_list()
    current = my_list["first"]
    for i in range(pos):
        current = current["next"]
    for i in range(num_elements):
        add_last(sublist, current["info"])
        current = current["next"]
    return sublist
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

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

def shell_sort(my_list, sort_crit):
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

def insertion_sort(my_list, sort_crit):
    size1 = size(my_list)
    pos1 = 1
    while pos1 < size1:
        pos2 = pos1
        while (pos2 > 0) and sort_crit(get_element(my_list, pos2), get_element(my_list, pos2 - 1)):
            exchange(my_list, pos2, pos2 - 1)
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