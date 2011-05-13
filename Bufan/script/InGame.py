# -*- coding:GBK -*-

import flashui
import log

pnl_inGame = None

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
	global pnl_inGame
	pnl_inGame = CInGamePanel()
	pnl_inGame.Show()
	
def choose_test(test_id):
	pnl_inGame.choose_test(test_id)
	
def Destory():
	pass
	
# ��Ϸ������
# 

def RequestLeaveRoom():
	pnl_inGame.Close()
	import Bufan_init
	Bufan_init.onClose(None)
	
def onGetScore():
	#TODO ������ʾ����
	pass
	