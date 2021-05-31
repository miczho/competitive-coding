import sys
from collections import defaultdict
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        n, m = len(servers), len(tasks)
        res = list()
        working = list()
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)

        time = 0
        for i in range(m):
            time = max(time, i)
            if not free:
                time = working[0][0]
            while working and working[0][0] <= time:
                heapq.heappush(free, heapq.heappop(working)[1])

            tmp = heapq.heappop(free)
            res.append(tmp[1])
            heapq.heappush(working, (time + tasks[i], tmp))

        return res


def main():
    s = Solution()
    print(s.assignTasks([3,3,2], [1,2,3,2,1,2]))


if __name__ == '__main__':
    main()