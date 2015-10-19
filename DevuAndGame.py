__author__ = 'daminglu'


class DevuAndGame:
    def canWin(self, nextLevel):
        visited = set([])
        to_visit = 0
        while True:
            print 'visiting ', to_visit
            if to_visit in visited:
                return "Lose"

            visited.add(to_visit)

            cur = nextLevel[to_visit]
            if cur == -1:
                return "Win"

            to_visit = cur



obj = DevuAndGame()

print obj.canWin([29,33,28,16,-1,11,10,14,6,31,7,35,34,8,15,17,26,12,13,22,1,20,2,21,-1,5,19,9,18,4,25,32,3,30,23,10,27])

# print obj.canWin([-1,1])