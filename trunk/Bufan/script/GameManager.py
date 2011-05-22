# -*- coding:GBK -*-

import iworld2d
import flashui
import MCreator
import Global
import WaitScreen
import PlayScreen

# 0-Wait 1-Play
gameState = 0
scr_wait = WaitScreen.WaitScreen()
scr_play = PlayScreen.PlayScreen()
thisHid = None
thatHid = None

sX = 327
sY = 127

def Initial():
	global  scr_wait	
	
	# 绘制面板
	scr_wait.Show()
	
def Destroy():
	global scr_wait, scr_play
	if scr_wait:
		scr_wait.Destory()
		scr_wait = None
	if scr_play:
		scr_play.Destory()
		scr_play = None

def MouseClick(mx, my):
		global gameState, scr_wait, scr_play
		if gameState == 0:
			scr_wait.onMouseClicked(mx, my)
		else:
			scr_play.onMouseClicked(mx, my)

def ChangeState(stateId):
	global gameState, scr_wait, scr_play
	if stateId == 1:
		scr_wait.Destroy()
		scr_wait = None
		scr_play = PlayScreen.PlayScreen()
		gameState = 1
	else:
		scr_play.Destroy()
		scr_play = None
		scr_wait = WaitScreen.WaitScreen()
		gameState = 0

# 网络消息回调
def onGetWelcome(msg):
	global thisHid
	thisHid = msg.hid
	
def onGetPlayerInfo(msg):
	global thisId, scr_wait, scr_play
	if stateId == 0:
		if msg.hid == thisId:
			scr_wait.SetPlayerInfo(0, msg.neckname, msg.win, msg.lose, msg.draw, msg.breakC)
		else: 
			scr_wait.SetPlayerInfo(1, msg.neckname, msg.win, msg.lose, msg.draw, msg.breakC)
	else:
		if msg.hid == thisId:
			scr_play.SetPlayerInfo(0, msg.neckname, msg.win, msg.lose, msg.draw, msg.breakC)
		else: 
			scr_play.SetPlayerInfo(1, msg.neckname, msg.win, msg.lose, msg.draw, msg.breakC)

#def on
	
	