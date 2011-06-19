import Global
import MCreator
import LocalChessBoard
import iavatar_ui

class WaitScreen():
	def __init__(self, thisInfo = None, thatInfo = None):
		self.bgImg = MCreator.CreateImage("Bufan/res/world2d/WaitBg.jpg", 0, 0, 1, 1, MCreator.BGLayer)
		self.ui = MCreator.CreateMovie('Bufan/res/gfx/WaitPanel.swf')
		self.thisAvatar = iavatar_ui.CAvatar("Bufan/res/ThisAvaBody.swf")
		self.thatAvatar = MCreator.CreateAvatar("Bufan/res/ThatAvaBody.swf")
		self.lChessBoard = LocalChessBoard.LocalChessBoard(319, 212, 396, 396)	# x, y, h, w
		self.isReady = 0

		if thisInfo:
			self.SetPlayerInfo(0, thisInfo.Nickname, thisInfo.Win, thisInfo.Lose, thisInfo.Draw, thisInfo.BreakC)
		if thatInfo:
			self.SetPlayerInfo(1, thatInfo.Nickname, thatInfo.Win, thatInfo.Lose, thatInfo.Draw, thatInfo.BreakC)
			
			
	def Show(self):
		self.ui.active = True
		self.ui.set_top()
		self.thisAvatar.add_player_avatar(Global.API.get_my_avatar())
		self.thisAvatar.show()
		self.thisAvatar.set_pos(5, 117)
		
		
		Global.Sound.play_music("Bufan/res/Music/InGame.mp3")

	def Destroy(self):
		self.bgImg.destroy()
		
		self.ui.active = False
		self.ui = None
		
		self.lChessBoard.Destroy()
		
		if self.thisAvatar:
			self.thisAvatar.destroy()
			self.thisAvatar = None
			
		if self.thatAvatar:
			self.thatAvatar.destroy()
			self.thatAvatar = None
			
	def OnMouseClicked(self, mPosX, mPosY):
		lastScore = self.lChessBoard.Score
		if self.lChessBoard.Click(mPosX, mPosY) == 0:
			# GameOver()
			pass
		else:
			thisScore = self.lChessBoard.Score
			if thisScore > lastScore:
				# Global.API.show_msg(str(thisScore - lastScore))
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

	
	
	
	
	
	
	
	
	
	
	
	