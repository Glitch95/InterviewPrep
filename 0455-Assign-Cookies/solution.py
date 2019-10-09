class Solution:
    def findContentChildren(self, g, s):
        # Solution 1 - Greedy Approach
        # O(nlogn) Time, O(1) Space

        # The idea is to iterate over the sorted cookie sizes and sorted greed factors.
        # If the current cookie size is greater than or equal to the current greed factor
        # we increment a count of the content children and move to the next greed factor
        # and content count. Else if the current cookie size is less than the current
        # greed factor, then that cookie cannot satisfy any of the remaining children,
        # so we move to the next cookie.

        # Sort the greed factors and the cookie sizes
        g.sort()
        s.sort()

        cookie_idx = child_idx = content_count = 0
        num_cookie, num_children = len(s), len(g)

        while cookie_idx < num_cookie and child_idx < num_children:
            greed_factor, cookie_size = g[child_idx], s[cookie_idx]

            if cookie_size < greed_factor:
                cookie_idx += 1             # Move to the next cookie
            else:
                content_count += 1
                cookie_idx += 1
                child_idx += 1

        return content_count

