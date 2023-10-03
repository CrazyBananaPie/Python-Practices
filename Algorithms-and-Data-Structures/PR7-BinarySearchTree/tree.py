from tree_node import TreeNode
from pr_2 import RAM, Generator


class SearchBinaryTree():
    def __init__(self):
        self.__tree_head: TreeNode = TreeNode(None)
        self.__child_status: dict = {"no_ch": '0', "1_ch_l": 'l1', "1_ch_r": 'r1', "2_ch": "2"}
        self.size: int = 0

    def insert(self, value: RAM, __index: int = None) -> bool:
        if not self.__tree_head.data:
            self.__tree_head.data = value
            self.size += 1
            return True

        self.__insertion_proc(self.__tree_head, value)
        self.size += 1
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
            self.__removing_head()
            self.size -= 1
            return True

        # All other "not head" situations
        else:
            return self.__removing_proc(value)

    def __removing_head(self):
        self.__def_ch_status(self.__tree_head)

        if self.__tree_head.ch_stat == '0':
            self.__tree_head = None
            return True

        elif self.__tree_head.ch_stat == 'r1':
            self.__tree_head.data = self.__tree_head.right.data
            self.__tree_head.right = None
            return True
        elif self.__tree_head.ch_stat == 'l1':
            self.__tree_head.data = self.__tree_head.left.data
            self.__tree_head.left = None
            return True

        elif self.__tree_head.ch_stat == '2':
            self.__two_ch_node_rm(self.__tree_head, self.__tree_head.right)
            return True

    def __removing_proc(self, value: RAM):
        current_node: TreeNode = self.find(value)
        if current_node is None:
            return False

        self.size -= 1
        parent_node: TreeNode = current_node.parent
        self.__def_ch_status(current_node)

        if current_node.ch_stat == '0':
            self.__no_ch_node_rm(parent_node, current_node)
            return True

        elif current_node.ch_stat == 'r1':
            self.__one_ch_node_rm(parent_node, current_node, current_node.right)
            return True
        elif current_node.ch_stat == 'l1':
            self.__one_ch_node_rm(parent_node, current_node, current_node.left)
            return True

        elif current_node.ch_stat == '2':
            self.__two_ch_node_rm(current_node, current_node.right)
            return True

    def __def_ch_status(self, node: TreeNode):
        # No children
        if not node.left and not node.right:
            node.ch_stat = self.__child_status['no_ch']

        # One child
        if node.left and not node.right:
            node.ch_stat = self.__child_status['1_ch_l']
        if not node.left and node.right:
            node.ch_stat = self.__child_status['1_ch_r']

        # Two children
        if node.left and node.right:
            node.ch_stat = self.__child_status['2_ch']

    @staticmethod
    def __no_ch_node_rm(parent_node: TreeNode, current_node: TreeNode):
        if parent_node.left == current_node:
            parent_node.left = None
        elif parent_node.right == current_node:
            parent_node.right = None

        return True

    @staticmethod
    def __one_ch_node_rm(parent_node: TreeNode, current_node: TreeNode, child_node: TreeNode) -> bool:
        if parent_node.left == current_node:
            parent_node.left = child_node
        elif parent_node.right == current_node:
            parent_node.right = child_node

        return True

    def __two_ch_node_rm(self, current_node: TreeNode, child_node: TreeNode) -> bool:
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

    def find(self, value: RAM) -> [TreeNode, None]:
        if value == self.__tree_head.data:
            return self.__tree_head

        return self.__find_proc(self.__tree_head, value)

    def __find_proc(self, current_node: TreeNode, value: RAM) -> [TreeNode, None]:

        if value == current_node.data:
            return current_node

        elif value > current_node.data and current_node.right:
            return self.__find_proc(current_node.right, value)
        elif value < current_node.data and current_node.left:
            return self.__find_proc(current_node.left, value)
        else:
            return None

    def find_by(self, attrs, values) -> [TreeNode, None]:
        template = dict(zip(attrs, values))
        values = list(template.values())

        if not self.__check_attr(template):
            print("ATTRIBUTE ERROR")
            return None

        return self.__find_by_proc(self.__tree_head, values, template)

    def __check_attr(self, template: dict) -> bool:
        if len(template) not in range(1, 7):
            return False
        for attr in template.keys():
            try:
                getattr(self.__tree_head.data, attr)
            except AttributeError:
                return False
        return True

    def __find_by_proc(self, current_node: TreeNode, values, template: dict) -> [TreeNode, None]:
        data_list = []
        for attr in template.keys():
            data_list.append(getattr(current_node.data, attr))

        if values == data_list:
            return current_node

        elif values > data_list and current_node.right:
            return self.__find_by_proc(current_node.right, values, template)
        elif values < data_list and current_node.left:
            return self.__find_by_proc(current_node.left, values, template)
        else:
            return None

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

    def min(self, current_node=None) -> object:
        if not current_node:
            current_node = self.__tree_head
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data

    def max(self, current_node=None) -> object:
        if not current_node:
            current_node = self.__tree_head
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.data

    def __len__(self):
        return self.size


g = Generator()
b = SearchBinaryTree()

a = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)

b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(a)
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())
b.insert(g.generate_single())

attrs = ['manufacturer', 'model', 'size']
values = ["Kingston", "ZP", 6]
print(b.find_by(attrs, values))
