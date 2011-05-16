# -*- coding:GBK -*-
# 游戏初始化

import iworld2d
import Global
import Message
import EventMap
import InGame
import game


def init(**args):
	gameId = int(args['gameid'])
	
	Global.init()

	# 注册回调
	Global.API.register_callback( gameId,
		Logic, Render, PostLogic,
		on_key_msg = onKeyMsg, 
		on_mouse_msg = onMouseMsg, 
		on_mouse_wheel =  onMouseWheel)

	# 初始化网络
	Global.API.register_game_room_msgdefine_and_callback(Message.MsgDefine, EventMap.GetEventMap())
	
	# 初始化显示
	iworld2d.init()

	# 开始游戏
	InGame.Initial()


def ForceDestroy():
	pass
	
# 回调函数
def Logic ():
	pass

	
def PostLogic ():
	pass
	
def Render ():
	pass
	
def onKeyMsg (msg, key_code):
	# 键盘事件回调
	pass


def onMouseMsg (msg, key):
	# 鼠标事件回调
	if msg == game.MSG_MOUSE_UP:
		if key == game.MOUSE_BUTTON_LEFT:
			InGame.MouseClick(game.mouse_x, game.mouse_y)
	pass


def onMouseWheel (msg, delta, key_state):
	# 鼠标滚轮事件回调
	pass
	
def onClose(eArgs):# 退出
	InGame.Destroy()
	iworld2d.destroy()
	Global.API.sender.cs_req_leave()