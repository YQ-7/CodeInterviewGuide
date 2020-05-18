import unittest


def is_match(s, exp):
    if s is None or exp is None:
        return False
    return process(s, exp, 0, 0) if is_valid(s, exp) else False


def process(s, e, si, ei):
    """
        s[si..slen]是否可以被e[ei..elen]匹配
    """
    if ei == len(e):
        return si == len(s)

    if ei + 1 == len(e) or "*" != e[ei + 1]:
        return si != len(s) \
               and (e[ei] == s[si] or e[ei] == ".") \
               and process(s, e, si + 1, ei + 1)
    while si != len(s) and (e[ei] == s[si] or e[ei] == "."):
        if process(s, e, si, ei + 2):
            return True
        si += 1
    return process(s, e, si, ei + 2)


def is_valid(s, e):
    """
        判断s、exp有效性
        s:不能含有"."、"*"
        exp:"*"不能是首字母，任意两个"*"不能相邻
    """
    for c in s:
        if c == "*" or c == ".":
            return False
    for i in range(len(e)):
        if e[i] == "*" and (i == 0 or e[i - 1] == "*"):
            return False
    return True


def is_match_dp(s, e):
    """
        动态规划算法 
    """
    if s is None or e is None or not is_valid(s, e):
        return False
    dp = init_dp(s, e)
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(e) - 2, -1, -1):
            if e[j + 1] != "*":
                dp[i][j] = (s[i] == e[j] or e[j] == ".") and dp[i + 1][j + 1]
            else:
                si = i
                while si != len(s) and (s[si] == e[j] or e[j] == "."):
                    if dp[si][j + 2]:
                        dp[i][j] = True
                        break
                    si += 1
                if not dp[i][j]:
                    dp[i][j] = dp[si][j + 2]
    return dp[0][0]


def init_dp(s, e):
    slen = len(s)
    elen = len(e)
    dp = [[False for i in range(elen + 1)] for j in range(slen + 1)]
    # 初始化s[len][elen]
    dp[slen][elen] = True
    # 初始化s[slen][0..elen]
    for j in range(elen - 2, -1, -1):
        if e[j] != "*" and e[j + 1] == "*":
            dp[slen][j] = True
        else:
            break
    # 初始化s[slen-1][elen-1]
    if slen > 0 and elen > 0:
        if e[elen - 1] == "." or s[slen - 1] == e[elen - 1]:
            dp[slen - 1][elen - 1] = True
    return dp


class MyTestCase(unittest.TestCase):
    def test_is_match(self):
        self.assertTrue(is_match("abc", "abc"))
        self.assertTrue(is_match("abc", "a.c"))
        self.assertTrue(is_match("abcd", ".*"))
        self.assertFalse(is_match("", "..*"))

    def test_is_match_dp(self):
        self.assertTrue(is_match_dp("abc", "abc"))
        self.assertTrue(is_match_dp("abc", "a.c"))
        self.assertTrue(is_match_dp("abcd", ".*"))
        self.assertFalse(is_match_dp("", "..*"))


if __name__ == '__main__':
    unittest.main()
