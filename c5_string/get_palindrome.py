import unittest


def get_palindrome_1(s):
    if s is None or len(s) < 2:
        return s
    # 计算字符串及子串变成回文需要添加的字符个数
    dp = get_dp(s)
    # 生成回文串
    res = [None] * (len(s) + dp[0][len(s) - 1])
    i = 0
    j = len(s) - 1
    res_l = 0
    res_r = len(res) - 1
    while i <= j:
        if s[i] == s[j]:
            res[res_l] = s[i]
            res_l += 1
            i += 1
            res[res_r] = s[j]
            res_r -= 1
            j -= 1
        elif dp[i][j - 1] < dp[i + 1][j]:
            res[res_l] = s[j]
            res_l += 1
            res[res_r] = s[j]
            res_r -= 1
            j -= 1
        else:
            res[res_l] = s[i]
            res_l += 1
            res[res_r] = s[i]
            res_r -= 1
            i += 1
    return "".join(res)


def get_dp(chas):
    dp = [[0] * len(chas) for v in range(len(chas))]
    for j in range(1, len(chas)):
        dp[j - 1][j] = 0 if chas[j - 1] == chas[j] else 1
        for i in range(j - 2, -1, -1):
            if chas[i] == chas[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp


class MyTestCase(unittest.TestCase):
    def test_get_palindrome_1(self):
        self.assertEqual("ABA", get_palindrome_1("AB"))
        self.assertEqual("A", get_palindrome_1("A"))
        self.assertEqual("AC1B2B1CA", get_palindrome_1("A1B21C"))


if __name__ == '__main__':
    unittest.main()
