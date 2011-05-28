# -*- coding:GBK -*-

import iworld2d
import flashui
import MCreator
import Global
import WaitScreen
import PlayScreen
import Bufan_init
import ChessHelper

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
	
	# �������
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
	# TODO ����������Ϣ ...
	
	# �л�״̬
	ChangeState(0)
	
# ������Ϣ�ص�
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
		scr_play.OnNetThisMove(msg.isOK)

def onNetThisRemove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisRemove(msg.isOK)

def onNetThisPutBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThisPutBubs(strToPoss(msg.positions))


def onNetThatPrepBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatPrepBubs(ChessHelper.StrToColors(msg.colors))
		

def onNetThatMove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatMove(msg.sX, msg.sY, msg.eX, msg.eY)
		
		

def onNetThatRemove(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatRemove(ChessHelper.StrToRemoves(msg.lineInfo))
		

def onNetThatPutBubs(msg):
	global gameState, scr_play
	if gameState == 1:
		scr_play.OnNetThatPutBubs(ChessHelper.StrToPoss(msg.positions))
		
	
















	
	
	
	
	