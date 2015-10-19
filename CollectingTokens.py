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
    result = "\nind: " + str(self.index) + ", val: "+ str(self.val)
    result += "\n"
    for c in self.children:
      # result += str(c)
      result += str(c.index)
      result += ", "
    result += "\n"
    return result


class CollectingTokens:

  def decideParent(self, nodes):
    q = []
    q.append(nodes[1])
    while len(q) > 0:
      curNode = q.pop(0)
      curNodeIndex = curNode.index
      for c in nodes[curNodeIndex].children:
        # del c[c.index(curNodeIndex)]
        for i, child in enumerate(c.children):
          if child.index == curNodeIndex:
            del c[i]
            break
        # del c.children[]
        q.append(c)




  def maxTokens(self, A, B, tokens, L):

    nodes = [TreeNode(token, i+1) for i, token in enumerate(tokens)]
    nodes.insert(0, TreeNode(-1))

    # create edges
    for i in range(0, len(A)):
      Ai = A[i]
      Bi = B[i]
      nodes[Ai].children.append(nodes[Bi])
      nodes[Bi].children.append(nodes[Ai])

    print nodes

    self.decideParent(nodes)
    print '\nAfter BFS\n'
    print nodes




obj = CollectingTokens()

A = [1, 2, 5, 3]
B = [4, 4, 1, 4]
tokens = [6, 1, 6, 4, 4]
L = 3

obj.maxTokens(A, B, tokens, L)