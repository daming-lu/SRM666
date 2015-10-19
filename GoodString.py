__author__ = 'daminglu'


class GoodString:
    def isGood(self, s):
        l = []
        for i in s:
            if i == 'a':
                l.append('a')
            elif i == 'b':
                if len(l) == 0:
                    return "Bad"
                l.pop()

        if len(l) == 0:
            return "Good"
        return "Bad"



