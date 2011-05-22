import Global
import GameObject
import LocalChessBoard

class PlayScreen():
	def __init__(self):
		self.bgImg = iworld2d.image2d("Bufan/res/world2d/background.jpg")
		self.bgImg.pos = (0, 0)
		
		self.ui = flashui.movie('Bufan/res/gfx/PlayPanel.swf', False, True, flashui.SM_NoScale)
		self.ui.align = flashui.Align_BottomCenter
		self.ui.enable_keyboard = False	# ui�㲻���ռ�����Ϣ
		self.now_test = None
		
		self.chessBoards = []
		self.chessBoards[0] = CliantChessBoard.ClientChessBoard(0, 127)
		self.chessBoards[1] = ClientChessBoard.ClientChessBoard(327, 127)

	def Show(self):
		self.bgImg.bring_to_front()
		
		self.ui.active = True
		self.ui.set_top()

	def Destory(self):
		self.ui.active = False
		self.ui = None
	
	def onMouseClicked(self, mPosX, mPosY):
			self.thisChessBoard.Click(mPosX, mPosY)
					
# ====================================================
# ����������Ϣ
# ====================================================
def onNetPrepBubs():
	#Global.API.
	pass

def onNetMove(self):
	Global.API.show_confirm("ѵ����Ϸ�������Ƿ�������", lChessBoard.Start(), None)
	
	
		
	
# ====================================================
# �����ص� - �����Ա
# ====================================================
def  onBreakClicked():
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
		