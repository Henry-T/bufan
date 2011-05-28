import MCreator
import flashui
import Global
import GameObject
import LocalChessBoard

class WaitScreen():
	def __init__(self):
		self.bgImg = MCreator.CreateImage("Bufan/res/world2d/background.jpg", 0, 0, 1, 1) 
		
		self.ui = flashui.movie('Bufan/res/gfx/WaitPanel.swf', False, True, flashui.SM_NoScale)
		self.ui.align = flashui.Align_BottomCenter
		self.ui.enable_keyboard = False	# ui层不接收键盘消息
		self.now_test = None
		
		self.lChessBoard = LocalChessBoard.LocalChessBoard(327, 127, 450, 450)
		
		self.isReady = 0

	def Show(self):
		self.ui.active = True
		self.ui.set_top()

	def Destroy(self):
		self.bgImg.destroy()
		
		self.ui.active = False
		self.ui = None
		
		self.lChessBoard.Destroy()
	
	def onMouseClicked(self, mPosX, mPosY):
		lastScore = lChessBoard.Score
		if self.lChessBoard.Click(mPosX, mPosY) == 0:
			GameOver()
		else:
			thisScore = self.lChessBoard.GetLastScore()
			if thisScore > lastScore:
				Global.API.show_msg(str(thisScore - lastScore))
				ui.lbl_localScore.label  = thisScore
	
	# ====================================================
	# UI 控制
	# ====================================================
	def SetPlayerInfo(self, which, nickname, win, lose, draw, breakC):
		if which == 0:
			self.ui.invoke("SetThisInfo", nickname, win, lose, draw, breakC)
		else:
			self.ui.invoke("SetThatInfo", nickname, win, lose, draw, breakC)
	
	
	# ====================================================
	# 本地训练游戏
	# ====================================================
	def localGameOver(self):
		Global.API.show_confirm("训练游戏结束！是否重来？", self.lChessBoard.Start(), None)
		
	
# ====================================================
# UI回调 - 非类成员
# ====================================================
def  onTrainClicked():
	import GameManager
	GameManager.scr_wait.lChessBoard.Start()

def onReadyClicked():
	import GameManager
	wait = GameManager.scr_wait
	if wait.isReady == 0:
		Global.API.sender.cs_setReady(isReady=1)
		wait.isReady = 1
	else:
		Global.API.sender.cs_setReady(isReady=0)
		wait.isReady = 0
	
def onLeaveClicked():
	import Bufan_init
	Bufan_init.onClose(None)
		