# -*- coding:GBK -*-

import flashui
import MCreator
import iworld2d
import Global
import ChessBoard

bgImg = None
pnl_inGame = None
chessBoard = None

sX = 327
sY = 127

class CInGamePanel(object):
	def __init__(self):
		self.movie = flashui.movie('Bufan/res/gfx/InGame.swf', False, True, flashui.SM_NoScale)
		self.movie.align = flashui.Align_BottomCenter
		self.movie.enable_keyboard = False	# ui�㲻���ռ�����Ϣ
		self.now_test = None

	def Show(self):
		self.movie.active = True
		self.movie.set_top()

	def Close(self):
		self.movie.active = False
		self.movie = None

	def choose_test(self, test_id):
		if self.now_test:
			self.now_test.destroy()
		m = __import__("hello_test%d"%test_id)
		if m:
			m.start()
			self.movie.invoke("set_tips", getattr(m, "TIPS", ""))
			self.now_test = m

def Initial():
	global bgImg, pnl_inGame
	
	# ���Ʊ���
	bgImg = iworld2d.image2d("Bufan/res/world2d/background.jpg")
	bgImg.pos = (0, 0)
	bgImg.bring_to_front()
	
	# ����flash���
	pnl_inGame = CInGamePanel()
	pnl_inGame.Show()
	
	# ������������
	global chessBoard
	chessBoard = ChessBoard.ChessBoard(sX, sY)
	
def choose_test(test_id):
	pnl_inGame.choose_test(test_id)
	
def Destroy():
	pnl_inGame.Close()
	
	global bgImg
	if bgImg:
		bgImg.destroy()
		bgImg = None
	
	chessBoard.Destroy()
	
def MouseClick(mx, my):
		if chessBoard:
			if chessBoard.Click(mx, my) == 0:
				GameOver()
			else:
				lastScore = chessBoard.GetLastScore()
				if lastScore > 0:
					Global.API.show_msg(str(lastScore))
				
				
# ��Ϸ����
def GameOver():
	Global.API.show_confirm("��Ϸʧ�ܣ��Ƿ�������", onRestart, RequestLeaveRoom)
	
def onRestart(arg):
	chessBoard.Restart()
	
def RequestLeaveRoom():
	import Bufan_init
	Bufan_init.onClose(None)
	
def onGetScore():
	#TODO ������ʾ����
	pass
	