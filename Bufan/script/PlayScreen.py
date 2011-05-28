import Global
import MCreator
import flashui
import GameObject
import LocalChessBoard	# TODO ������
import ClientChessBoard
import MirrorChessBoard

class PlayScreen():
	def __init__(self):
		self.bgImg = MCreator.CreateImage("Bufan/res/world2d/background_play.jpg", 0, 0, 1, 1)
		self.bgImg.pos = (0, 0)
		
		self.ui = flashui.movie('Bufan/res/gfx/PlayPanel.swf', False, True, flashui.SM_NoScale)
		self.ui.align = flashui.Align_BottomCenter
		self.ui.enable_keyboard = False	# ui�㲻���ռ�����Ϣ
		self.now_test = None
		
		self.chessBoards = []
		self.chessBoards.append(ClientChessBoard.ClientChessBoard(514, 130, 450, 450))
		self.chessBoards.append(MirrorChessBoard.MirrorChessBoard(52, 112, 270, 270))

	def Show(self):
		self.bgImg.bring_to_front()
		
		self.ui.active = True
		self.ui.set_top()

	def Destroy(self):
		self.bgImg.destroy()
		
		self.ui.active = False
		self.ui = None
		
		self.chessBoards[0].Destroy()
		self.chessBoards[1].Destroy()
	
	def onMouseClicked(self, mPosX, mPosY):
			self.chessBoards[0].Click(mPosX, mPosY)
					
# ====================================================
# ����������Ϣ
# ====================================================
def onNetThisPrepBubs(colors):
	self.chessBoards[0].OnNetPrepSlots(colors)

def onNetThisMove(isOk):
	if valide == 1:
		self.chessBoards[0].OnNetMove(isOk)

def onNetThisRemove(isOk):
	if valid == 1
		self.chessBoards[0].OnNetRemove(isOk)

def onNetThisPutBubs(poss):
	self.chessBoards[0].OnNetPutBubs(poss)

	
def onNetThatPrepBubs(colors):
	self.chessBoards[1].OnNetPrepSlots(colors)
	
def onNetThatMove(points):
	self.chessBoards[1].OnNetMove(points)

def onNetThatRemove(removes):
	self.chessBoards[1].OnNetRemove(removes)

def onNetThatPutBubs(poss):
	self.chessBoards[1].OnNetPutSlots(poss)
	
	
		
	
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
		