import Global
import MCreator
import LocalChessBoard

class WaitScreen():
	def __init__(self):
		self.bgImg = MCreator.CreateImage("Bufan/res/world2d/background.jpg", 0, 0, 1, 1, MCreator.BGLayer)
		self.ui = MCreator.CreateMovie('Bufan/res/gfx/WaitPanel.swf')
		self.lChessBoard = LocalChessBoard.LocalChessBoard(302, 129, 450, 450)
		self.isReady = 0

	def Show(self):
		self.ui.active = True
		self.ui.set_top()

	def Destroy(self):
		self.bgImg.destroy()
		
		self.ui.active = False
		self.ui = None
		
		self.lChessBoard.Destroy()
	
	def OnMouseClicked(self, mPosX, mPosY):
		lastScore = self.lChessBoard.Score
		if self.lChessBoard.Click(mPosX, mPosY) == 0:
			# GameOver()
			pass
		else:
			thisScore = self.lChessBoard.Score
			if thisScore > lastScore:
				Global.API.show_msg(str(thisScore - lastScore))
				self.ui.invoke("SetTrainScore", thisScore)
	
	
	
	# ====================================================
	# 本地训练游戏
	# ====================================================
	def localGameOver(self):
		Global.API.show_confirm("训练游戏结束！是否重来？", self.lChessBoard.Start(), None)
		
	
	# ====================================================
	# UI回调
	# ====================================================
	def  OnTrainClicked(self):
			self.lChessBoard.Restart()
			self.ui.invoke("SetTrainScore", 0)

	def OnReadyClicked(self, _isReady):
		Global.Sender.cs_setReady(isReady=_isReady)
		
	def OnLeaveClicked(self):
		import Bufan_init
		Bufan_init.onClose(None)
		
	# ====================================================
	# UI控制
	# ====================================================
	def SetPlayerInfo(self, which, nickname, win, lose, draw, breakC):
		if which == 0:
			self.ui.invoke("SetThisInfo", nickname, win, lose, draw, breakC)
		else:
			self.ui.invoke("SetThatInfo", nickname, win, lose, draw, breakC)
	
	def SetReady(self, which, isReady):
		self.ui.invoke("UIReady", which, isReady)

	
	
	
	
	
	
	
	
	
	
	
	