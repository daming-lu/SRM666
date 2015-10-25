__author__ = 'daminglu'

"""
{1,2,5,3}
{4,4,1,4}
{6,1,6,4,4}
3
Returns: 16
"""

class TreeNode:
  def __init__(self, x, i=0):
    self.val = x
    self.index = i
    self.children = []

  def __repr__(self):
    result = "\nind: " + str(self.index) + ", val: " + str(self.val)
    result += "\n"
    for c in self.children:
      result += str(c)
      # result += str(c.index)
      result += ", "
    result += "\n"
    return result


class CollectingTokens:

  def decideParent(self, nodes):
    q = []
    q.append(1)
    while len(q) > 0:
      curNodeIndex = q.pop(0)
      for c in nodes[curNodeIndex].children:
        # del c[c.index(curNodeIndex)]
        del nodes[c].children[nodes[c].children.index(curNodeIndex)]
        # del c.children[]
        q.append(c)

  def f(self, x, e, L, m):
    if self.matrix[x][e][L][m] != -1:
      return self.matrix[x][e][L][m]

    # cur = self.f(x, e+1, L, m)
    cur = 0
    if e < len(self.nodes[x].children):
      y = self.nodes[x].children[e]
      for subL in range(0, L+1):
        if L-subL >= 2:
          # can do a back and forth on u
          tm = self.tokens[y-1] + self.f(y, 0, subL, 1) + self.f(x, e+1, L-2-subL, m)
          cur = max(cur, tm)
        if L-subL >=1 and m == 0:
          # pick y as the last one (dig into it)
          tm = self.tokens[y-1] + self.f(y, 0, subL, 0) + self.f(x, e+1, L-1-subL, 1)
          cur = max(cur, tm)

      cur = max(cur, self.f(x, e+1, L, m))

    self.matrix[x][e][L][m] = cur
    return cur



  def maxTokens(self, A, B, tokens, L):

    self.nodes = [TreeNode(token, i+1) for i, token in enumerate(tokens)]
    self.nodes.insert(0, TreeNode(-1))
    self.tokens = tokens
    # create edges
    for i in range(0, len(A)):
      Ai = A[i]
      Bi = B[i]
      self.nodes[Ai].children.append(Bi)
      self.nodes[Bi].children.append(Ai)

    # print self.nodes

    self.decideParent(self.nodes)
    # print '\nAfter BFS\n'
    # print self.nodes
    #
    # print '\nGo on ...\n'

    # rangeNode = 51
    # rangeL = 101
    # rangeM = 2
    rangeNode = len(self.tokens) + 1
    rangeL = L + 1
    rangeM = 2

    # rangeNode = 3
    # rangeL = 5
    # rangeM = 2

    self.matrix = [[[[-1 for m in range(0, rangeM)]
                for L in range(0, rangeL)]
                  for e in range(0, rangeNode)]
                    for x in range(0, rangeNode)]

    # for x in range(0, rangeNode):
    #   for e in range(0, rangeNode):
    #     for L in range(0, rangeL):
    #       for m in range(0, rangeM):
    #         print x, e, L, m,  self.matrix[x][e][L][m]
          # print "\n"
    # print matrix

    return self.f(1, 0, L, 0) + self.tokens[0]


obj = CollectingTokens()
# t1
A = [1, 2, 5, 3]
B = [4, 4, 1, 4]
tokens = [6, 1, 6, 4, 4]
L = 3

print obj.maxTokens(A, B, tokens, L)

# t2
A = [9,1,7,10,5,8,3,4,2]
B = [6,6,9,6,6,1,1,6,6]
tokens = [4,2,1,6,3,7,8,5,2,9]
L = 4

print obj.maxTokens(A, B, tokens, L)



