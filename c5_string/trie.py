import unittest


class TreeNode(object):
    """
    搜索树节点,存储a~z
    """

    def __init__(self):
        self.path = 0  # 记录元素
        self.end = 0
        self.map = [None] * 26


class Trie(object):
    """
    搜索树
    """

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        """
        插入元素work
        """
        if word is None:
            return
        node = self.root
        node.path += 1
        for c in word:
            index = ord(c) - ord('a')
            if node.map[index] is None:
                node.map[index] = TreeNode()
            node = node.map[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        """
        判断word是否存在
        """
        if word is None:
            return False
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.map[index] is None:
                return False
            node = node.map[index]
        return node.end != 0

    def delete(self, word):
        """
        删除work，有多个时只删除一个
        """
        if not self.search(word):
            return
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            node.map[index].path -= 1
            if node.map[index].path == 0:
                node.map[index] = None
                return
            node = node.map[index]
        node.end -= 1

    def prefix_number(self, pre):
        """
        统计以pre为前缀的元素个数
        """
        if pre is None:
            return 0
        node = self.root
        for c in pre:
            index = ord(c) - ord('a')
            if node.map[index] is None:
                return 0
            node = node.map[index]
        return node.path


class MyTestCase(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("abc"))
        trie.insert("abc")
        trie.insert("abcd")
        trie.insert("b")
        self.assertTrue(trie.search("abc"))
        trie.insert("b")
        trie.delete("b")
        self.assertTrue(trie.search("b"))
        trie.delete("b")
        self.assertFalse(trie.search("b"))


if __name__ == '__main__':
    unittest.main()
