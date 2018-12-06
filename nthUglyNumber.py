import heapq


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    uglies = [1, 2, 3, 4, 5]

    def nthUglyNumber(self, n):
        # write your code here
        if n <= len(self.uglies):
            return self.uglies[n - 1]
        newUglys = [1]
        i = 0
        while i < len(self.uglies):
            a = self.uglies[i]
            k = i
            while k < len(self.uglies):
                b = self.uglies[k]
                newUglys.append(a * b)
                k += 1
            i += 1
        newUglys = list(set(newUglys))
        newUglys.sort()
        self.uglies = newUglys
        print(self.uglies)
        return self.nthUglyNumber(n)

    def nthUglyNumber1(self, n):
        heap = [1]
        visited = set([1])
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for multi in [2, 3, 5]:
                if val * multi not in visited:
                    visited.add(val * multi)
                    heapq.heappush(heap, val * multi)
                print('heap:\t', heap)
                print('visited:\t', visited)
        return val

    def nthUglyNumber2(self, n):
        arr = [1]
        n2, n3, n5 = 0, 0, 0
        # d = {1: {1: 1}}
        for i in range(1, n):
            minN = min([arr[n2] * 2, arr[n3] * 3, arr[n5] * 5])
            if minN >= arr[n2] * 2:  # 当前保存的下一个数大于指针上的数，指针向后移动一位
                n2 += 1
                # tmp = {2: n2}
            if minN >= arr[n3] * 3:
                n3 += 1
                # tmp = {3: n3}
            if minN >= arr[n5] * 5:
                n5 += 1
                # tmp = {5: n5}
            # d[minN] = tmp
            arr.insert(i, minN)
            i += 1
        '''

        for a in d:
            print(i, a, dict.get(d, a))
            i += 1
        print(arr)
        i = 1
        '''

        return arr[n - 1]
s = Solution()
print(s.nthUglyNumber2(2312312849))
