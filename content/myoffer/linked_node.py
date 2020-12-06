class LinkNode():
    def __init__(self, value):
        self.value = value
        self.next = None


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def delete_duplicate_node(node: LinkNode) -> LinkNode:
    if node == None or node.next == None:
        return node

    next: LinkNode = node.next

    if next.value == node.value:
        while next.value == next.value:
            next = next.next
        return delete_duplicate_node(next)
    else:
        node.next = delete_duplicate_node(next)
        return node


def recur_reverse_link(head: LinkNode) -> LinkNode:
    if head == None or head.next == None:
        return head

    next = head.next
    head.next = None

    new_head = recur_reverse_link(next)
    next.next = head

    return new_head


def reverse_link_by_insert_head1(head: LinkNode) -> LinkNode:
    if head == None or head.next == None:
        return head

    node = head
    new_head = head.next
    head = new_head.next
    new_head.next = node

    while head is not None:
        next = new_head
        new_head = head
        head = head.next
        new_head.next = next

    return node


def reverse_link_by_insert_head2(head: LinkNode) -> LinkNode:
    if head == None or head.next == None:
        return head

    node = LinkNode(-1)

    while head is not None:
        new_link_head = head
        head = head.next

        new_link_head.next = node
        node = new_link_head

    return node


def merge(link1: LinkNode, link2: LinkNode) -> LinkNode:
    if link1 is None: return link2
    if link2 is None: return link1

    if link1.value < link2.value:
        link1.next = merge(link1.next, link2)
        return link1

    link2.next = merge(link1, link2.next)
    return link2


def mirror_tree(tree: TreeNode) -> TreeNode:
    if tree is None: return tree
    treeNode = tree.left
    tree.left = tree.right
    tree.right = treeNode

    mirror_tree(tree.left)
    mirror_tree(tree.right)

    return tree


class ClockWiseData:
    def __init__(self, matrix):
        self.__matrix = matrix

    def __out_clockwise_data(self, matrix):
        if matrix is None or len(matrix) == 0: return None
        col = len(matrix[0])
        if col == 0: return matrix[0]

        row = len(matrix)

        if row > 2:
            data_len = col * 2 + (row - 2) * 2
        else:
            data_len = col * 2

        row_data_last_index = data_len - 1 - (row - 2)

        data = [data_len]

        for i in range(col):
            data[i] = matrix[0, i]
            data[row_data_last_index - i] = matrix[row - 1, i]

        for i in range(1, row - 1):
            data[col + i] = matrix[i, col - 1]
            data[data_len - i] = matrix[row, 0]

        return data

    def out(self):
        row_start, col_start = 0
        row_end = len(self.__matrix)
        col_end = len(self.__matrix[0])

        data = [row_end * col_end]

        matrix = self.__matrix

        while len(matrix):
            data.extend(self.__out_clockwise_data(matrix[row_start:row_end,][col_start:col_end]))
            row_start = row_start + 1
            col_start = col_start + 1
            row_end = row_end - 1
            col_end = row_end - 1

        return data