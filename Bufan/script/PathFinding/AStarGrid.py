import AStarNode

class AStarGrid:
	def __init__(self, sizeX, sizeY,  sPos, ePos, obstacles):
		self.SizeX =  sizeX
		self.SizeY = sizeY
		
		self.Nodes = []
		for i in range(0, self.SizeX):
			self.Nodes.append([])
			for j in range(0, self.SizeY):
				isObs = 0
				if obstacles.count([i, j]) == 1:
					isObs = 1
				self.Nodes[i].append(AStarNode.AStarNode(i, j, isObs))
				
		self.StartNode =  self.Nodes[sPos[0]][sPos[1]]
		self.EndNode =  self.Nodes[ePos[0]][ePos[1]]
		
		
	def GetNeighborNodes(self, node):
		nNodes = []
		if node.X > 0 and not self.Nodes[node.X - 1][node.Y].IsObstacle:
			nNodes.append(self.Nodes[node.X - 1][node.Y ])
		if node.X < self.SizeX - 1 and  not self.Nodes[node.X + 1][node.Y].IsObstacle:
			nNodes.append(self.Nodes[node.X + 1][node.Y])
		if node.Y > 0 and  not self.Nodes[node.X][node.Y - 1].IsObstacle:
			nNodes.append(self.Nodes[node.X][node.Y - 1])
		if node.Y < self.SizeY - 1 and  not self.Nodes[node.X][node.Y + 1].IsObstacle:
			nNodes.append(self.Nodes[node.X][node.Y + 1])
		return nNodes
		
	
	