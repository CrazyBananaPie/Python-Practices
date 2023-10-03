class TreeNode:
    def __init__(self, data=None):
        # Info in node
        self.data = data
        self.ch_stat: str = "Unknown"

        # Links on other nodes
        self.left = None
        self.right = None
        self.parent: [TreeNode, None] = None

    def __repr__(self):
        return f'TreeNode(Data: {self.data},  Left link: {self.left is not None},  ' \
               f'Right link: {self.right is not None})'
