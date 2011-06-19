import Global
import MCreator
import GameManager
import ClientChessBoard
import MirrorChessBoard

class PlayScreen():
	def __init__(self, thisInfo = None, thatInfo = None):
		self.bgImg = None
		self.bgImg = MCreator.CreateImage("Bufan/res/world2d/PlayBg.jpg", 0, 0, 1, 1, MCreator.BGLayer)
		self.bgImg.pos = (0, 0)
		self.ui = MCreator.CreateMovie('Bufan/res/gfx/PlayPanel.swf')
		self.chessBoards = []
		self.chessBoards.append(ClientChessBoard.ClientChessBoard(514, 130, 450, 450))
		self.chessBoards.append(MirrorChessBoard.MirrorChessBoard(52, 112, 270, 270))

		if thisInfo:
			self.SetPlayerInfo(0, thisInfo.Nickname, thisInfo.Win, thisInfo.Lose, thisInfo.Draw, thisInfo.BreakC)
		if thatInfo:
			self.SetPlayerInfo(1, thatInfo.Nickname, thatInfo.Win, thatInfo.Lose, thatInfo.Draw, thatInfo.BreakC)
			
	def Show(self):
		#self.bgImg.bring_to_front()
		
		self.ui.active = True
		self.ui.set_top()

	def Destroy(self):
		if self.bgImg:
			self.bgImg.destroy()
		
		self.ui.active = False
		self.ui = None
		
		self.chessBoards[0].Destroy()
		self.chessBoards[1].Destroy()
	
	def OnMouseClicked(self, mPosX, mPosY):
		self.chessBoards[0].Click(mPosX, mPosY)
			
	def OnGameOver(self, whichWin):
		pass
					
	# ====================================================
	# 棋盘网络信息
	# ====================================================
	def OnNetThisPrepBubs(self, colors):
		self.chessBoards[0].OnNetPrepSlots(colors)

	def OnNetThisMove(self, isOk):
		if isOk == 1:
			self.chessBoards[0].OnNetMove(isOk)

	def OnNetThisRemove(self, isOk, score):
		if isOk == 1:
			self.chessBoards[0].OnNetRemove(isOk)
			self.ui.invoke("SetScore", 0, score)

	def OnNetThisPutSlots(self, poss):
		self.chessBoards[0].OnNetPutSlots(poss)

		
	def OnNetThatPrepBubs(self, colors):
		self.chessBoards[1].OnNetPrepSlots(colors)
		
	def OnNetThatMove(self, points):
		self.chessBoards[1].OnNetMove(points)

	def OnNetThatRemove(self, removes, score):
		self.chessBoards[1].OnNetRemove(removes)
		self.ui.invoke("SetScore", 1, score)

	def OnNetThatPutBubs(self, poss):
		self.chessBoards[1].OnNetPutSlots(poss)
		
		
			
		
	# ====================================================
	# 交互回调 - 非类成员
	# ====================================================
	def OnBreakClicked():
		# GameManager.scr_wait.chessBoards[1].Start()
		pass
		
	def SetPlayerInfo(self, which, nickname, win, lose, draw, breakC):
		if which == 0:
			self.ui.invoke("SetThisInfo", nickname, win, lose, draw, breakC)
		else:
			self.ui.invoke("SetThatInfo", nickname, win, lose, draw, breakC)
			
	def OnTick(time):
		self.ui.invoke("SetCountDownTime", time)