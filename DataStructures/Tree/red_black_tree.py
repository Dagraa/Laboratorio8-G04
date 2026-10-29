from DataStructures.Tree import rbt_node

def default_compare(key, element):
    element_key = rbt_node.get_key(element)
    if key < element_key:
        return -1
    if key > element_key:
        return 1
    return 0

def size_tree(node):
    return 0 if node is None else node["size"]

def is_red(node):
    return node is not None and node["color"] == rbt_node.RED

def flip_node_color(node):
    if node is not None:
        node["color"] = rbt_node.BLACK if is_red(node) else rbt_node.RED
        
def flip_colors(node):
    if node is None or node["left"] is None or node["right"] is None:
        return
    flip_node_color(node)
    flip_node_color(node["left"])
    flip_node_color(node["right"])
    
def rotate_left(node):
    child = node["right"]
    if child is None:
        return node
    node["right"] = child["left"]
    child["left"] = node
    child["color"] = node["color"]
    node["color"] = rbt_node.RED
    child["size"] = node["size"]
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return child

def rotate_right(node):
    child = node["left"]
    if child is None:
        return node
    node["left"] = child["right"]
    child["right"] = node
    child["color"] = node["color"]
    node["color"] = rbt_node.RED
    child["size"] = node["size"]
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return child

def insert_node(node, key, value):
    if node is None:
        return rbt_node.new_node(key, value, rbt_node.RED)
    comparison = default_compare(key, node)
    if comparison < 0:
        node["left"] = insert_node(node["left"], key, value)
    elif comparison > 0:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value
    if is_red(node["right"]) and not is_red(node["left"]):
        node = rotate_left(node)
    if is_red(node["left"]) and is_red(node["left"]["left"]):
        node = rotate_right(node)
    if is_red(node["left"]) and is_red(node["right"]):
        flip_colors(node)
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return node

def new_map():
    return {"root": None, "type": "RBT", "size": 0}

def put(my_map, key, value):
    old_value = get(my_map, key)
    my_map["root"] = insert_node(my_map["root"], key, value)
    my_map["root"]["color"] = rbt_node.BLACK
    if old_value is None:
        my_map["size"] += 1
    return my_map

def get(my_map, key):
    current = my_map["root"]
    while current is not None:
        comparison = default_compare(key, current)
        if comparison < 0:
            current = current["left"]
        elif comparison > 0:
            current = current["right"]
        else:
            return current["value"]
    return None
def size(my_map):
    return size_tree(my_map["root"])
