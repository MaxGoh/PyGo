class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def search_list(node, item):
    if not node or not node.value:
        return None

    if (node.value == item):
        return node

    else:
        return search_list(node.next, item)


def insert_list(node, item):
    if not node:
        return None

    if node.next:
        return insert_list(node.next, item)

    else:
        temp_node = Node(item)
        node.next = temp_node


def predecessor_list(node, item):
    if not node or not node.next:
        return None

    if (node.next.value == item):
        return node

    else:
        return predecessor_list(node.next, item)


def delete_list(node, item):
    search_node = search_list(node, item)

    if search_node:
        pred = predecessor_list(node, item)

        if not pred:
            node = pred.next

        else:
            pred.next = search_node.next


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c

    # Search List
    print('Search List: ', search_list(a, 1))
    print('Search List: ', search_list(a, 2))
    print('Search List: ', search_list(a, 3))

    print('Search List: ', search_list(a, 9))

    # Insert List
    insert_list(a, 4)
    insert_list(a, 5)
    print('Insert List 4: ', a.next.next.next.value)
    print('Insert List 5: ', a.next.next.next.next.value)

    # Delete List
    print('Before deletion: ', search_list(a, 3).value)
    delete_list(a, 3)
    print('After deletion: ', search_list(a, 3))
