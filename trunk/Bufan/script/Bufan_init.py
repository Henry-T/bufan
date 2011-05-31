# -*- coding:GBK -*-
# ��Ϸ��ʼ��

import MCreator
import Input
import Global
import Message
import EventMap
import GameManager


def init(**args):
	Global.init()
	Global.API.register_callback(int(args['gameid']),
		Logic, Render, None,
		on_key_msg = None, 
		on_mouse_msg = onMouseMsg, 
		on_mouse_wheel =  None)
	Global.API.register_game_room_msgdefine_and_callback(Message.MsgDefine, EventMap.EventMap)
	MCreator.initial()
	GameManager.Initial()
	
def Logic ():
	# TODO ��������
	pass
	
	
def Render ():
	# TODO ����Ч��
	pass

def onMouseMsg (msg, key):
	if Input.IsLeftClicked(msg, key):
		GameManager.MouseClick(Input.MouseX(), Input.MouseY())
	
def onClose(eArgs):# �˳�
	GameManager.Destroy()
	Global.Sender.cs_reqLeave()
	Global.Destroy()
	
	
#def PostLogic ():
#	pass

#def ForceDestroy():
#	pass
