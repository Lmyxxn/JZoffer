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


# Deserialization
class Codec:

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
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

