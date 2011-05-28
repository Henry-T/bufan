import AStarGrid

class PathFinder:
	# 4方向A*寻路
	# 这个方案中诱导权重和距离权重相同，因此公用midH函数
	def __init__(self):
		self.openList = []
		self.closeList = []
		self.Path =  []
		
		self.grid = None
	
	def SetGrid(self, aStarGrid):
		self.grid = aStarGrid
		grid = self.grid
		grid.StartNode.G = 0
		grid.StartNode.H = self.midH(grid.StartNode, grid.EndNode)
		grid.StartNode.F = grid.StartNode.G + grid.StartNode.H
	
	def FindPath(self):
		grid = self.grid
		self.openList = []
		self.closeList = []
		
		curNode  = grid.StartNode
		endNode = grid.EndNode
		
		self.openList.append(curNode)
		while len(self.openList) > 0:
			# 获取开放集中F最小的节点
			lowFNode = self.openList[0]
			for i in range(1, len(self.openList)):
				if self.openList[i].F < lowFNode.F:
					lowFNode = self.openList[i]
			
			if lowFNode == endNode:
				return self.constructPath(endNode)
			
			self.openList.remove(lowFNode)
			self.closeList.append(lowFNode)
			
			# 搜索临域
			for node in grid.GetNeighborNodes(lowFNode):
				if self.nodeInList(node, self.closeList):
					continue
				tempG =  lowFNode.G + self.midH(node, lowFNode)
				betterNode = 0
				if self.nodeInList(node, self.openList) == 0:
					self.openList.append(node)
					betterNode = 1
				elif tempG < node.G:
					betterNode = 1
				else :
					betterNode = 0
					
				if betterNode == 1:
					node.Parent = lowFNode
					node.G = tempG
					node.H = self.midH(node, endNode)
					node.F  = node.G + node.H
					
		return []
		
	def nodeInList(self, node, list):
		if list.count(node) == 1:
			return 1
		else:
			return 0
		
	def midH(self, node1, node2):
		dX = node1.X - node2.X
		dY = node1.Y - node2.Y
		h = dX + dY
		return h
		
		
	def constructPath(self, node):
		path = []
		if node.Parent:
			path.extend(self.constructPath(node.Parent))
		path.append(node)
		return path
		