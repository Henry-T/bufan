# -*- coding:GBK -*-
# 游戏初始化

import MCreator
import Input
import Global
import Message
import EventMap
import GameManager


def init(**args):
	Global.init()
	Global.API.register_callback( int(args['gameid']),
		Logic, Render, None,
		on_key_msg = None, 
		on_mouse_msg = onMouseMsg, 
		on_mouse_wheel =  None)
	Global.API.register_game_room_msgdefine_and_callback(Message.MsgDefine, EventMap.EventMap)
	MCreator.initial()
	GameManager.Initial()
	
def Logic ():
	# TODO 动画更新
	pass
	
	
def Render ():
	# TODO 动画效果
	pass

def onMouseMsg (msg, key):
	if Input.IsLeftClicked():
		GameManager.MouseClick(game.mouse_x, game.mouse_y)
	
def onClose(eArgs):# 退出
	GameManager.Destroy()
	iworld2d.destroy()
	Global.Sender.cs_req_leave()
	
	
#def PostLogic ():
#	pass

#def ForceDestroy():
#	pass
