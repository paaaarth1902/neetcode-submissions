class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum, rightSum, maxSum = 0, 0, 0

        # [1,2,3,4,5,6,1]

        for i in range(k):
            leftSum += cardPoints[i]
        maxSum = leftSum

        rightIdx = len(cardPoints) - 1

        for i in range((k-1),-1, -1):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[rightIdx]
            rightIdx -= 1
            maxSum = max(maxSum, (leftSum + rightSum))

        return maxSum


        