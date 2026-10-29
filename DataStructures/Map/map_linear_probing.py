import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False
def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1
def find_slot(my_map, key, hash_value):
   first_avail = None
   for _ in range(my_map["capacity"]):
      entry = lt.get_element(my_map["table"], hash_value)
      entry_key = me.get_key(entry)
      if entry_key is None:
         return False, hash_value if first_avail is None else first_avail
      if entry_key == "__EMPTY__":
         if first_avail is None:
            first_avail = hash_value
      elif entry_key == key:
         return True, hash_value
      hash_value = (hash_value + 1) % my_map["capacity"]
   return False, first_avail

def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, hash_value)
    return ocupied

def get(my_map,key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, hash_value)
    if not ocupied:
        return None
    entry = lt.get_element(my_map["table"], slot)
    return me.get_value(entry)

def new_map(n_elements = 500 ,load_factor = 0.7, prime = 109345121):
   
   try:
        capacity = mf.next_prime(int(n_elements / load_factor))
        scale = random.randint(1, prime - 1)
        shift = random.randint(0, prime - 1)
        new_table = dict(
            n_elements = n_elements,
            prime = prime,
            limit_factor = load_factor,
            current_factor = 0,
            capacity = capacity,
            scale = scale,
            shift = shift,
            table = None,
            size = 0,
            type = "LINEAR_PROBING")
        new_table["table"] = lt.new_list()
        i = 0
        while i < capacity:
         entry = me.new_map_entry(None, None)
         lt.add_last(new_table["table"], entry)
         i += 1
        return new_table
   except Exception as e:
       print("Hubo un error:", e)
   return None


def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    occupied, slot_index = find_slot(my_map, key, hash_value)
    if occupied:
       tombstone = me.new_map_entry("__EMPTY__", "__EMPTY__")
       lt.change_info(my_map["table"], slot_index, tombstone)
       my_map["size"] -= 1
    return my_map


def rehash(my_map):
   old_table = my_map["table"]
   my_map["capacity"] = mf.next_prime(my_map["capacity"] * 2)
   my_map["table"] = lt.new_list()
   my_map["size"] = 0
   my_map["current_factor"] = 0
   i = 0
   while i < my_map["capacity"]:
      lt.add_last(my_map["table"], me.new_map_entry(None, None))
      i += 1
   i = 0
   while i < lt.size(old_table):
      old_entry = lt.get_element(old_table, i)
      old_key = me.get_key(old_entry)
      if old_key is not None and old_key != "__EMPTY__":
         put(my_map, old_key, me.get_value(old_entry))
      i += 1
   return my_map


def size(my_map):
    return my_map["size"]


def put(mp: dict, key: object, value: object) -> dict:
   try:
      _hash = mf.hash_value(mp, key)
      entry = me.new_map_entry(key, value)
      occupied, idx = find_slot(mp, key, _hash)
      lt.change_info(mp["table"], idx, entry)
      if not occupied:
         mp["size"] += 1
         mp["current_factor"] = mp["size"] / mp["capacity"]
      if mp["current_factor"] > mp["limit_factor"]:
         mp = rehash(mp)
      return mp
   except Exception as exp:
      print("error", exp)
def is_empty(my_map):
   return my_map["size"] == 0
def key_set(my_map):
   keys = lt.new_list()
   i = 0
   while i < lt.size(my_map["table"]):
      entry = lt.get_element(my_map["table"], i)
      key = me.get_key(entry)
      if key is not None and key != "__EMPTY__":
         lt.add_last(keys, key)
      i += 1
   return keys
def value_set(my_map):
   values = lt.new_list()
   i = 0
   while i < lt.size(my_map["table"]):
      entry = lt.get_element(my_map["table"], i)
      key = me.get_key(entry)
      if key is not None and key != "__EMPTY__":
         lt.add_last(values, me.get_value(entry))
      i += 1
   return values