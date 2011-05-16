class AStarNode:
	def __init__(self, x, y, isObstacle = 0):
		self.X = x
		self.Y = y
		self.F = 0
		self.G = 0
		self.H = 0
		self.Parent = None
		self.IsObstacle = isObstacle
		
	