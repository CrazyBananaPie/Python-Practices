from typing import Optional

from abstract_classes import AbstractList
from models_and_generators import RAM


class SimpleList(AbstractList):
    def __init__(self):
        self.__body: list = []
        self.size: int = 0

    def add(self, value: RAM, index: int = None) -> bool:
        if index is None:
            self.__body.append(value)
            self.size += 1
            return True
        elif index not in range(self.size):
            return False
        else:
            self.__body.insert(index, value)
            self.size += 1
            return True

    def insert(self, value: RAM, index: int) -> bool:
        if index not in range(self.size):
            return False
        else:
            self.__body[index] = value
            return True

    def find(self, value: RAM) -> int:
        if value not in self.__body:
            return False
        else:
            return self.__body.index(value)

    def get(self, index: int) -> RAM | None:
        if index not in range(self.size):
            return None
        else:
            return self.__body[index]

    def remove(self, value: RAM) -> bool:
        if self.size == 0 or value not in self.__body:
            return False
        else:
            self.__body.remove(value)
            self.size -= 1
            return True

    def sort(self) -> bool:
        self.__body.sort()
        return True

    def get_all(self) -> list:
        return self.__body

    def __repr__(self):
        return f'{self.get_all()}'


class TreeNode:
    def __init__(self, data):
        # Info in node
        self.data = data
        self.child_status = "Unknown"

        # Links on other nodes
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent: Optional[TreeNode] = None

    def __repr__(self):
        return f'TreeNode(Data: {self.data},  Left link: {self.left is not None},  ' \
               f'Right link: {self.right is not None})'


class BinaryTree:
    def __init__(self):
        self.__tree_head = TreeNode(None)
        self.__child_status = {
            "no_children": "0",
            "1_child_left": "l1",
            "1_child_right": "r1",
            "2_children": "2"
        }
        self.__size = 0

    def insert(self, value: RAM) -> bool:
        if not self.__tree_head.data:
            self.__tree_head.data = value
            self.__size += 1
            return True

        self.__insertion_proc(self.__tree_head, value)
        self.__size += 1
        return True

    def __insertion_proc(self, current_node: TreeNode, value: RAM) -> bool:
        if value >= current_node.data and not current_node.right:
            current_node.right = TreeNode(value)
            current_node.right.parent = current_node
            return True
        elif value < current_node.data and not current_node.left:
            current_node.left = TreeNode(value)
            current_node.left.parent = current_node
            return True

        if value >= current_node.data and current_node.right:
            self.__insertion_proc(current_node.right, value)
        elif value < current_node.data and current_node.left:
            self.__insertion_proc(current_node.left, value)

    def remove(self, value: RAM) -> bool:
        # If there are no tree
        if self.__tree_head is None:
            return False

        # If we are working with head of the tree
        if value == self.__tree_head.data:
            self.__size -= 1
            return self.__removing_head()
        # All other "not head" situations
        else:
            self.__size -= 1
            return self.__removing_process(value)

    def __removing_head(self):
        self.__define_node_child_status(self.__tree_head)

        if self.__tree_head.child_status == '0':
            self.__tree_head = None

        elif self.__tree_head.child_status == 'r1':
            self.__tree_head.data = self.__tree_head.right.data
            self.__tree_head.right = None

        elif self.__tree_head.child_status == 'l1':
            self.__tree_head.data = self.__tree_head.left.data
            self.__tree_head.left = None

        elif self.__tree_head.child_status == '2':
            self.__node_w_two_children_removal(self.__tree_head, self.__tree_head.right)

        return True

    def __removing_process(self, value: RAM) -> bool:
        current_node: TreeNode = self.find(value)
        if current_node is None:
            return False

        parent_node: TreeNode = current_node.parent
        self.__define_node_child_status(current_node)

        if current_node.child_status == "0":
            return self.__node_w_no_child_removal(parent_node, current_node)

        elif current_node.child_status in ("r1", "l1"):
            return self.__node_w_one_child_removal(
                parent_node,
                current_node,
                current_node.right if current_node.child_status == "r1" else current_node.left)

        elif current_node.child_status == "2":
            return self.__node_w_two_children_removal(current_node, current_node.right)



    def __define_node_child_status(self, node: TreeNode):
        # No children
        if not node.left and not node.right:
            node.child_status = self.__child_status['no_children']

        # One child
        if node.left and not node.right:
            node.child_status = self.__child_status['1_child_left']
        if not node.left and node.right:
            node.child_status = self.__child_status['1_child_right']

        # Two children
        if node.left and node.right:
            node.child_status = self.__child_status['2_children']

    @staticmethod
    def __node_w_no_child_removal(parent_node: TreeNode, current_node: TreeNode) -> bool:
        if parent_node.left == current_node:
            parent_node.left = None
        elif parent_node.right == current_node:
            parent_node.right = None

        return True

    @staticmethod
    def __node_w_one_child_removal(parent_node: TreeNode, current_node: TreeNode, child_node: TreeNode) -> bool:
        if parent_node.left == current_node:
            parent_node.left = child_node
        elif parent_node.right == current_node:
            parent_node.right = child_node

        return True

    def __node_w_two_children_removal(self, current_node: TreeNode, child_node: TreeNode) -> bool:
        while child_node.left:
            child_node = child_node.left

        buffer = child_node.data
        self.remove(child_node.data)
        current_node.data = buffer

        return True

    def replace(self, value: RAM, new_value: RAM) -> bool:
        node = self.find(value)
        if node is not None:
            node.data = new_value
            return True
        else:
            return False

    def find(self, value: RAM, __current_node: TreeNode = None) -> TreeNode | None:
        if not __current_node:
            __current_node = self.__tree_head

        if value == __current_node.data:
            return __current_node

        elif value > __current_node.data and __current_node.right:
            return self.find(value, __current_node.right)
        elif value < __current_node.data and __current_node.left:
            return self.find(value, __current_node.left)
        else:
            return None

    def find_by(self, attrs: list, values: list, __current_node: TreeNode = None) -> TreeNode | None:
        if not __current_node:
            if not self.__check_attrs_and_values(attrs, values):
                return None

            __current_node = self.__tree_head

        data_list = []
        for attr in attrs:
            data_list.append(getattr(__current_node.data, attr))

        if values == data_list:
            return __current_node

        elif values > data_list and __current_node.right:
            return self.find_by(attrs, values, __current_node.right)
        elif values < data_list and __current_node.left:
            return self.find_by(attrs, values, __current_node.left)
        else:
            return None

    def __check_attrs_and_values(self, attrs: list, values: list) -> bool:
        if len(attrs) not in range(1, 7):
            print("ERROR: Quantity of attributes in invalid")
            return False
        elif len(attrs) != len(values):
            print("ERROR: Amount of values should be the same as amount of attributes")
            return False
        for attr in attrs:
            try:
                getattr(self.__tree_head.data, attr)
            except AttributeError:
                print(f"ERROR: Attribute with name '{attr}' doesn't exist")
                return False
        return True

    def get_all(self) -> list:
        body = []
        self.__depth_path(self.__tree_head, body)
        body.sort()
        return body

    def __depth_path(self, current_node: TreeNode, body: list):
        if current_node is None:
            return False

        if current_node.left is not None:
            self.__depth_path(current_node.left, body)
        if current_node.right is not None:
            self.__depth_path(current_node.right, body)
        body.append(current_node.data)

    def min(self, current_node=None) -> RAM:
        if not current_node:
            current_node = self.__tree_head
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data

    def max(self, current_node=None) -> RAM:
        if not current_node:
            current_node = self.__tree_head
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data

    def __len__(self) -> int:
        return self.__size
