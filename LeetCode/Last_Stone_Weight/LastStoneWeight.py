# Last Stone Weight
# Solution
# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone(or 0 if there are no stones left.)


# Example 1:

# Input: [2, 7, 4, 1, 8, 1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to[2, 4, 1, 1, 1] then,
# we combine 2 and 4 to get 2 so the array converts to[2, 1, 1, 1] then,
# we combine 2 and 1 to get 1 so the array converts to[1, 1, 1] then,
# we combine 1 and 1 to get 0 so the array converts to[1] then that's the value of last stone.


# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# Hint  # 1
# Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn.


class Solution:

    def findHighestStone(self, stones):
        highest = float('-inf')
        position = -1
        for stone in range(len(stones)):
            if stones[stone] > highest:
                highest = stones[stone]
                position = stone

        return position

    def lastStoneWeight(self, list):

        while len(stones) > 1:

            y = self.findHighestStone(stones)
            y = stones.pop(y)
            x = self.findHighestStone(stones)
            x = stones.pop(x)

            if y != x:
                y = y - x
                stones.append(y)
            elif y == x:
                continue

        if len(stones) == 1:
            return stones[0]

        elif len(stones) == 0:
            return 0


S = Solution()
stones = [2, 7, 4, 1, 8, 1]

if S.lastStoneWeight(stones) == 1:
    print("That's the correct answer")
else:
    print("that's wrong")
