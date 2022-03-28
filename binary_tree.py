from __future__ import annotations
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class TreeNode:
    value: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def printTree(self):
        c = Codec()
        print(c.serialize(self))


# Serialization
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
            """Decodes your encoded data to tree.
            :type data: str
            :rtype: TreeNode
            """
            def rdeserialize(l):
                """ a recursive helper function for deserialization."""
                if l and l[0].lower() == 'n':
                    l.pop(0)
                    return None

                root = TreeNode(l[0])
                l.pop(0)
                root.left = rdeserialize(l)
                root.right = rdeserialize(l)
                return root

            data_list = data.split(',')
            root = rdeserialize(data_list)
            return root

def main():
    c = Codec()
    root = c.deserialize(data='1,2,3,4,n,n,5,6,7,8')
    root.printTree()


if __name__ == "__main__":
    main()
