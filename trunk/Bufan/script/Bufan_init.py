# -*- coding:GBK -*-
# ��Ϸ��ʼ��

import iworld2d
import Global
import Message
import EventMap
import InGame


def init(**args):
	gameId = int(args['gameid'])
	
	Global.init()

	# ע��ص�
	Global.API.register_callback( gameId,
		Logic, Render, PostLogic,
		on_key_msg = onKeyMsg, 
		on_mouse_msg = onMouseMsg, 
		on_mouse_wheel =  onMouseWheel)

	# ��ʼ������
	Global.API.register_game_room_msgdefine_and_callback(Message.MsgDefine, EventMap.GetEventMap())
	
	# ��ʼ��Ϸ
	InGame.Initial()

	iworld2d.init()


def ForceDestroy():
	pass
	
# �ص�����
def Logic ():
	pass

	
def PostLogic ():
	pass
	
def Render ():
	pass
	
def onKeyMsg (msg, key_code):
	# �����¼��ص�
	pass


def onMouseMsg (msg, key):
	# ����¼��ص�
	pass


def onMouseWheel (msg, delta, key_state):
	# �������¼��ص�
	pass
	
def onClose (eArgs):
	# �˳�
	# Global.API.sender.hw_cs_leave_room()	# ����������˳���Ϣ
	InGame.Destory()
	iworld2d.destroy()