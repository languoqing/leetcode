"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
"""
"""动态规划"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(cost[i] + dp[i-2],cost[i] + dp[i-1])
            #print('dp[{}]=={}'.format(i,dp[i]))
        return min(dp[len(dp)-1],dp[len(dp)-2])

if __name__ == '__main__':
    a = Solution()
    c = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = a.minCostClimbingStairs(c)
    print(res)