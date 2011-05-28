# -*- coding:GBK -*-

import iworld2d
import flashui
import MCreator
import Global
import WaitScreen
import PlayScreen
import Bufan_init

# 0-Wait 1-Play
gameState = 0
scr_wait = None  #WaitScreen.WaitScreen()
scr_play = None #PlayScreen.PlayScreen()
thisHid = None
thatHid = None

sX = 327
sY = 127

def Initial():
	global  scr_wait	
	
	# 绘制面板
	scr_wait = WaitScreen.WaitScreen()
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
		scr_play.Show()
		gameState = 1
	else:
		scr_play.Destroy()
		scr_play = None
		scr_wait = WaitScreen.WaitScreen()
		scr_wait.Show()
		gameState = 0

def GetReady():
	ChangeState(1);
	
def RequestLeaveRoom():
	Bufan_init.onClose(None)

def Break():
	# TODO 发送网络信息 ...
	
	# 切换状态
	ChangeState(0)
	
# 网络消息回调
def onNetWelcome(msg):
	global thisHid
	thisHid = msg.chid
	
def onNetPlayerInfo(msg):
	global gameState, thisHid, scr_wait, scr_play
	if gameState == 0:
		if msg.hid == thisHid:
			scr_wait.SetPlayerInfo(0, msg.nickname, msg.win, msg.lose, msg.draw, msg.breakC)
		else: 
			scr_wait.SetPlayerInfo(1, msg.nickname, msg.win, msg.lose, msg.draw, msg.breakC)
	else:
		if msg.hid == thisHid:
			scr_play.SetPlayerInfo(0, msg.nickname, msg.win, msg.lose, msg.draw, msg.breakC)
		else: 
			scr_play.SetPlayerInfo(1, msg.nickname, msg.win, msg.lose, msg.draw, msg.breakC)

def onNetPlayerReady(msg):
	global gameState, scr_wait
	if gameState == 0:
		if msg.hid == thisHid:
			scr_wait.SetPlayerReady(0, msg.isReady)
		else:
			scr_wait.SetPlayerReady(1, msg.isReady)
	
def onNetPlayerLeft(msg):
	global gameState, thatHid, scr_wait
	if gameState == 0:
		if msg.hid == thatHid:
			scr_wait.OnPlayerLeave()

			
def onNetThisPrepBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisPrepBubs(strToColors(msg.colors))
	
def onNetThisMove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisMove()

def onNetThisRemove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisRemove()

def onNetThisPutBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisPutBubs(strToPoss(msg.positions))


def onNetThatPrepBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatPrepBubs(strToColors(msg.colors))
		

def onNetThatMove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatMove(msg.sX, msg.sY, msg.eX, msg.eY)
		
		

def onNetThatRemove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatRemove(strToRemoves(msg.lineInfo))
		

def onNetThatPutBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatPutBubs(strToPoss(msg.positions))
		
		
def strToColors(colorStr):
	colors = []
	for i in range(0, len(colorStr)):
		colors.append(int(ord(colorStr[i, 1])))
	return colors
	
def strToPoss(posStr):
	poss = []
	for i in range(0, len(posStr)):
		poss.append(int(ord(posStr[i, 1])))
	return poss

def strToRemoves(removeNum,removeStr):s
	removes = []
	for i in range(0, removeNum):
		removes.append([])
		for j in range(0, 4):
			removes[i].append(int(ord(removeStr[i * 4 + j, 1])))
	return removes


















	
	
	
	
	