class Solution:
    def maxProfit(self, prices):
        # Solution 1 - Greedy Approach
        # O(n) Time, O(1) Space

        # We notice that the points of interest are the peaks and
        # valleys of the prices when plotted on a graph. If we subtract
        # the each valley from the next peak we will get the
        # max profit possible.

        # if not prices:
        #     return 0
        # i = j = 0
        # profit = 0
        # l = len(prices) - 1
        # while i < l:
        #     while i < l and prices[i] > prices[i+1]:
        #         i += 1
        #     j = i
        #     while j < l and prices[j] < prices[j+1]:
        #         j += 1
        #     if i < j:
        #         profit += prices[j] - prices[i]
        #     i = j + 1
        # return profit

        # Solution 2 - Greedy Approach
        # O(n) Time, O(1) Space

        # This is similar to Solution 1 except that instead of looking for every peak
        # following a valley, we can simply go on crawling over the slope and keep on
        # adding the profit obtained from every consecutive transaction. In the end,
        # we will be using the peaks and valleys effectively.

        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit

