class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        count = 0
        targetStr = str(k)
        for number in range(0,n+1):
            ss = str(number)
            cc = ss.count(targetStr)
            print(number,cc,end='\n')
            count = count + cc
        return count

print(Solution().digitCounts(1,12))