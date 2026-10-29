from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node


def new_map(cmpfunction=None):
    return {"root": None, "cmpfunction": cmpfunction}


def _compare(key, node_key, cmpfunction):
    if cmpfunction is not None:
        result = cmpfunction(key, node_key)
        return (result > 0) - (result < 0)
    return (key > node_key) - (key < node_key)


def get(my_map, key):
    node = my_map["root"]
    while node is not None:
        comparison = _compare(key, node["key"], my_map.get("cmpfunction"))
        if comparison == 0:
            return node["value"]
        node = node["left"] if comparison < 0 else node["right"]
    return None


def size(bst):
    return bst["root"]["size"] if bst.get("root") is not None else 0


def _node_size(node):
    return node["size"] if node is not None else 0


def put(bst, key, value):
    bst["root"] = _insert(bst.get("root"), key, value, bst.get("cmpfunction"))
    return bst


def _insert(root, key, value, cmpfunction):
    if root is None:
        return bst_node.new_node(key, value)
    comparison = _compare(key, root["key"], cmpfunction)
    if comparison < 0:
        root["left"] = _insert(root["left"], key, value, cmpfunction)
    elif comparison > 0:
        root["right"] = _insert(root["right"], key, value, cmpfunction)
    else:
        root["value"] = value
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root


def remove(bst, key):
    bst["root"] = _remove(bst.get("root"), key, bst.get("cmpfunction"))
    return bst


def _remove(root, key, cmpfunction):
    if root is None:
        return None
    comparison = _compare(key, root["key"], cmpfunction)
    if comparison < 0:
        root["left"] = _remove(root["left"], key, cmpfunction)
    elif comparison > 0:
        root["right"] = _remove(root["right"], key, cmpfunction)
    else:
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]
        successor = _min_node(root["right"])
        root["key"], root["value"] = successor["key"], successor["value"]
        root["right"] = _delete_min(root["right"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root


def contains(my_bst, key):
    return get(my_bst, key) is not None


def is_empty(my_bst):
    return my_bst.get("root") is None


def key_set(my_bst):
    keys = al.new_list()
    return key_set_tree(my_bst.get("root"), keys)


def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        al.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list


def value_set(my_bst):
    values = al.new_list()
    return value_set_tree(my_bst.get("root"), values)


def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        al.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list


def _min_node(root):
    while root is not None and root["left"] is not None:
        root = root["left"]
    return root


def _max_node(root):
    while root is not None and root["right"] is not None:
        root = root["right"]
    return root


def get_min(bst):
    node = _min_node(bst.get("root"))
    return node["key"] if node is not None else None


def get_max(bst):
    node = _max_node(bst.get("root"))
    return node["key"] if node is not None else None


def delete_min(bst):
    bst["root"] = _delete_min(bst.get("root"))
    return bst


def _delete_min(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = _delete_min(root["left"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root


def delete_max(bst):
    bst["root"] = _delete_max(bst.get("root"))
    return bst


def _delete_max(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = _delete_max(root["right"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root


def floor(bst, key):
    node = _floor(bst.get("root"), key, bst.get("cmpfunction"))
    return node["key"] if node is not None else None


def _floor(root, key, cmpfunction):
    if root is None:
        return None
    comparison = _compare(key, root["key"], cmpfunction)
    if comparison == 0:
        return root
    if comparison < 0:
        return _floor(root["left"], key, cmpfunction)
    candidate = _floor(root["right"], key, cmpfunction)
    return candidate if candidate is not None else root


def ceiling(bst, key):
    node = _ceiling(bst.get("root"), key, bst.get("cmpfunction"))
    return node["key"] if node is not None else None


def _ceiling(root, key, cmpfunction):
    if root is None:
        return None
    comparison = _compare(key, root["key"], cmpfunction)
    if comparison == 0:
        return root
    if comparison > 0:
        return _ceiling(root["right"], key, cmpfunction)
    candidate = _ceiling(root["left"], key, cmpfunction)
    return candidate if candidate is not None else root


def select(bst, position):
    if position < 0 or position >= size(bst):
        return None
    node = bst.get("root")
    while node is not None:
        left_size = _node_size(node["left"])
        if position < left_size:
            node = node["left"]
        elif position > left_size:
            position -= left_size + 1
            node = node["right"]
        else:
            return node["key"]
    return None


def rank(bst, key):
    node = bst.get("root")
    result = 0
    cmpfunction = bst.get("cmpfunction")
    while node is not None:
        comparison = _compare(key, node["key"], cmpfunction)
        if comparison < 0:
            node = node["left"]
        else:
            result += 1 + _node_size(node["left"])
            if comparison == 0:
                break
            node = node["right"]
    return result


def height(bst):
    def tree_height(node):
        if node is None:
            return 0
        return 1 + max(tree_height(node["left"]), tree_height(node["right"]))
    return tree_height(bst.get("root"))


def keys(bst, low=None, high=None):
    result = al.new_list()
    if low is None:
        low = get_min(bst)
    if high is None:
        high = get_max(bst)
    if low is None or high is None:
        return result

    def visit(node):
        if node is None:
            return
        cmpfunction = bst.get("cmpfunction")
        if _compare(node["key"], low, cmpfunction) >= 0:
            visit(node["left"])
        if _compare(node["key"], low, cmpfunction) >= 0 and _compare(
                node["key"], high, cmpfunction) <= 0:
            al.add_last(result, node["key"])
        if _compare(node["key"], high, cmpfunction) <= 0:
            visit(node["right"])

    visit(bst.get("root"))
    return result


def values(bst, low=None, high=None):
    result = al.new_list()
    for key in keys(bst, low, high)["elements"]:
        al.add_last(result, get(bst, key))
    return result
