import math


class ClimbStair:
    def __init__(self, n):
        self.n = n

    def climb1(self):
        steps = [self.n]

        steps[1] = 1
        steps[2] = 2

        for i in range(1, self.n):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[self.n - 1]

    def climb2(self):
        pre_step1 = 1
        pre_step2 = 2

        for i in range(1, self.n):
            cur = pre_step1 + pre_step2
            pre_step1 = pre_step2
            pre_step2 = cur

        return pre_step2


class RobOneStreet:
    def rob_a_street(self, values):
        pre1, pre2 = 0, 0

        for i in range(0, len(values)):
            cur = max(pre1 + values[i], pre2)
            pre1 = pre2
            pre2 = cur

        return pre2


class RobCycleStreet:
    def rob(self, values):
        l = len(values)
        return max(self.__rob(values[:l - 1]), self.__rob(values[:l - 2]))

    def __rob(self, values):
        pre1, pre2 = 0, 0

        for i in range(0, len(values)):
            cur = max(pre1 + values[i], pre2)
            pre1 = pre2
            pre2 = cur

        return pre2


class PathCalculation:
    def same_weight_path(self, values):
        n = len(values[0])
        result = [n]
        for value in values:
            result[0] = result[0] + value[0]
            for i in range(1, n):
                result[i] = max(result[i], result[i - 1]) + values[i]
        return result[n - 1]


class CharacterEdit():
    def min_edit(self, str1, str2):
        if str1 is None or len(str1) == 0:
            return 0 if str2 is None else len(str2)
        if str2 is None or len(str2) == 0:
            return 0 if str1 is None else len(str1)

        m, n = len(str1), len(str2)
        dp = []

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if str1[i] == str2[j]:
                    dp[i][i] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return dp[m][n]
