import iworld2d
import Global
import GameObject
import LocalChessBoard

class WaitScreen():
	def __init__(self):
		self.bgImg = iworld2d.image2d("Bufan/res/world2d/background.jpg")
		self.bgImg.pos = (0, 0)
		
		self.ui = flashui.movie('Bufan/res/gfx/WaitPanel.swf', False, True, flashui.SM_NoScale)
		self.ui.align = flashui.Align_BottomCenter
		self.ui.enable_keyboard = False	# ui层不接收键盘消息
		self.now_test = None
		
		lChessBoard = LocalChessBoard.LocalChessBoard(327, 127)
		
		self.isReady = 0

	def Show(self):
		self.bgImg.bring_to_front()
		
		self.ui.active = True
		self.ui.set_top()

	def Destory(self):
		self.ui.active = False
		self.ui = None
	
	def onMouseClicked(self, mPosX, mPosY):
			if lChessBoard.Click(mx, my) == 0:
				GameOver()
			else:
				lastScore = lChessBoard.GetLastScore()
				if lastScore > 0:
					Global.API.show_msg(str(lastScore))
					ui.lbl_localScore.label  = lChessBoard.Score  # TODO
	
	# ====================================================
	# UI 控制
	# ====================================================
	def SetPlayerInfo(which, neckname, win, lose, draw, breakC):
		if which == 0:
			ui.invoke(SetThisInfo, neckname, win, lose, draw, breakC)
		else:
			ui.invoke(SetThatInfo, neckname, win, lose, draw, breakC)
	
	
	# ====================================================
	# 本地训练游戏
	# ====================================================
	def localGameOver(self):
		Global.API.show_confirm("训练游戏结束！是否重来？", lChessBoard.Start(), None)
		
	
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
		