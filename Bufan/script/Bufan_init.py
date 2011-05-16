# -*- coding:GBK -*-
# ��Ϸ��ʼ��

import iworld2d
import Global
import Message
import EventMap
import InGame
import game


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
	
	# ��ʼ����ʾ
	iworld2d.init()

	# ��ʼ��Ϸ
	InGame.Initial()


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
	if msg == game.MSG_MOUSE_UP:
		if key == game.MOUSE_BUTTON_LEFT:
			InGame.MouseClick(game.mouse_x, game.mouse_y)
	pass


def onMouseWheel (msg, delta, key_state):
	# �������¼��ص�
	pass
	
def onClose(eArgs):# �˳�
	InGame.Destroy()
	iworld2d.destroy()
	Global.API.sender.cs_req_leave()