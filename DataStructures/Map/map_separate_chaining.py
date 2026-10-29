import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import single_linked_list as sl
def default_compare(key, element):
    """Compara una llave con una entrada del mapa. Retorna 0, 1 o -1."""
    if key == me.get_key(element):
        return 0
    elif key > me.get_key(element):
        return 1
    return -1
def rehash(my_map):
    old_table = my_map["table"]
    my_map["capacity"] = mf.next_prime(my_map["capacity"] * 2)
    my_map["table"] = lt.new_list()
    my_map["size"] = 0
    my_map["current_factor"] = 0
    i = 0
    while i < my_map["capacity"]:
        lt.add_last(my_map["table"], sl.new_list())
        i += 1
    for index in range(lt.size(old_table)):
        bucket = lt.get_element(old_table, index)
        for position in range(sl.size(bucket)):
            entry = sl.get_element(bucket, position)
            put(my_map, me.get_key(entry), me.get_value(entry))
    return my_map
def new_map(num_elements=500, load_factor=4, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    my_map = dict(
        prime=prime,
        capacity=capacity,
        scale=scale,
        shift=shift,
        table=None,
        current_factor=0,
        limit_factor=load_factor,
        size=0,
        type="SEPARATE_CHAINING")
    my_map["table"] = lt.new_list()
    i = 0
    while i < capacity:
        lt.add_last(my_map["table"], sl.new_list())
        i += 1
    return my_map
def put(my_map, key, value):
    idx = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], idx)
    found = False
    i = 0
    while i < sl.size(bucket) and not found:
        entry = sl.get_element(bucket, i)
        if default_compare(key, entry) == 0:
            me.set_value(entry, value)
            found = True
        i += 1
    if not found:
        sl.add_last(bucket, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    return my_map
def contains(my_map, key):
    idx = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], idx)
    found = False
    i = 0
    while i < sl.size(bucket) and not found:
        if default_compare(key, sl.get_element(bucket, i)) == 0:
            found = True
        i += 1
    return found
def get(my_map, key):
    idx = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], idx)
    result = None
    found = False
    i = 0
    while i < sl.size(bucket) and not found:
        entry = sl.get_element(bucket, i)
        if default_compare(key, entry) == 0:
            result = me.get_value(entry)
            found = True
        i += 1
    return result
def remove(my_map, key):
    idx = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], idx)
    found = False
    i = 0
    while i < sl.size(bucket) and not found:
        if default_compare(key, sl.get_element(bucket, i)) == 0:
            sl.delete_element(bucket, i + 1)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
            found = True
        i += 1
    return my_map
def size(my_map: dict) -> int:
    return my_map['size']


def is_empty(my_map: dict) -> bool:
    return my_map["size"] == 0


def key_set(my_map: dict):
    keys = lt.new_list()
    for index in range(lt.size(my_map["table"])):
        bucket = lt.get_element(my_map["table"], index)
        for position in range(sl.size(bucket)):
            lt.add_last(keys, me.get_key(sl.get_element(bucket, position)))
    return keys

def value_set(my_map: dict):
    values = lt.new_list()
    for index in range(lt.size(my_map["table"])):
        bucket = lt.get_element(my_map["table"], index)
        for position in range(sl.size(bucket)):
            lt.add_last(values, me.get_value(sl.get_element(bucket, position)))
    return values 
    
    