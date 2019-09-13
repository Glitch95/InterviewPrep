class Solution:
    def trap(self, height):
        # SOLUTION 1 - Dynamic Programming
        # O(n) Time O(n) Space

        # The water trapped above a bar is the
        # height of water that is above it,
        # since the width is 1.
        # This works out to be min of the max height to
        # the left and the max height to the right
        # less the height of the bar itself.

        # if not height:
        #     return 0
        #
        # n = len(height)
        # max_left = [None] * n
        # max_right = [None] * n
        #
        # max_left[0] = height[0]
        # for i in range(1, n):
        #     max_left[i] = max(max_left[i - 1], height[i])
        #
        # max_right[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     max_right[i] = max(max_right[i + 1], height[i])
        #
        # trapped_water = 0
        # for i in range(n):
        #     trapped_water += min(max_left[i], max_right[i]) - height[i]
        #
        # return trapped_water

        # SOLUTION 2 - Using a Stack
        # O(n) Time O(n) Space

        # We keep a stack and iterate over the array.
        # We add the index of the bar to the stack
        # if bar is smaller than or equal to the
        # bar at top of stack, which means that the
        # current bar is bounded by the previous bar
        # in the stack. If we found a bar longer than
        # that at the top, we are sure that the bar at
        # the top of the stack is bounded by the current
        # bar and a previous bar in the stack, hence,
        # we can pop it and add resulting trapped water
        # to the result.

        # if not height:
        #     return 0

        # n = len(height)
        # stack = []
        # trapped_water = 0

        # for i in range(n):
        #     while stack and height[i] > height[stack[-1]]:
        #         top = stack.pop()
        #         if not stack:
        #             break
        #         distance = i - stack[-1] - 1
        #         bounded_height = min(height[stack[-1]], height[i]) - height[top]
        #         trapped_water += distance * bounded_height
        #     stack.append(i)

        # return trapped_water

        # SOLUTION 3 - Using 2 pointers
        # O(n) Time and O(1) Space
        
        # From the figure in dynamic programming approach, notice that as long as
        # right_max[i] > left_max[i], the water trapped depends upon the left_max,
        # and similar is the case when left_max[i] > right_max[i]. 
        # So, we can say that if there is a larger bar at one end (say right),
        # we are assured that the water trapped would be dependant on height of bar
        # in current direction (from left to right). As soon as we find the bar at
        # other end (right) is smaller, we start iterating in opposite direction 
        # (from right to left). 
        # We must maintain left_max and right_max during the iteration, 
        # but now we can do it in one iteration using 2 pointers, switching between the two.
        
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        trapped_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    trapped_water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    trapped_water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        
        return trapped_water 

