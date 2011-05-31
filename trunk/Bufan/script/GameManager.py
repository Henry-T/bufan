import Global
import WaitScreen
import PlayScreen
import Bufan_init
import ChessHelper

State = "Wait"
scr_wait = None
scr_play = None
thisHid = None
thisReady = 0
thatHid = None
thatReady = 0

def Initial():
	global  scr_wait
	scr_wait = WaitScreen.WaitScreen()
	scr_wait.Show()
	
def Destroy():
	global scr_wait, scr_play
	if scr_wait:
		scr_wait.Destroy()
		scr_wait = None
	if scr_play:
		scr_play.Destroy()
		scr_play = None

def MouseClick(mx, my):
	global State, scr_wait, scr_play
	if State == "Wait":
		scr_wait.OnMouseClicked(mx, my)
	else:
		print("对战中点击")
		scr_play.OnMouseClicked(mx, my)
		
	
def ChangeState(state):
	global State, scr_wait, scr_play
	if state == "Play":
		scr_wait.Destroy()
		scr_wait = None
		scr_play = PlayScreen.PlayScreen()
		scr_play.Show()
		State = "Play"
	else:
		scr_play.Destroy()
		scr_play = None
		scr_wait = WaitScreen.WaitScreen()
		scr_wait.Show()
		State = "Wait"

def SetReady():
	Global.Sender.cs_setReady(isReady=1)

def SetNotReady():
	Global.Sender.cs_setReady(isReady=0)
	

def onNetWelcome(msg):
	global thisHid
	thisHid = msg.chid
	
def onNetPlayerInfo(msg):
	global State, thisHid, scr_wait, scr_play
	if State == "Wait":
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
	global State, scr_wait, thisReady, thatReady
	if State == "Wait":
		if msg.hid == thisHid:
			thisReady = msg.isReady
			scr_wait.SetReady(0, msg.isReady)
		else:
			thatReady = msg.isReady
			scr_wait.SetReady(1, msg.isReady)
			
	if thisReady and thatReady:
		# 加入倒计时 [服务器端计时3秒后才切入游戏，其间接受客户端的退出请求(需要优化协议)]
		ChangeState("Play")
	
def onNetPlayerLeft(msg):
	global State, thatHid, scr_wait
	if State == "Wait":
		if msg.chid == thatHid:
			scr_wait.OnPlayerLeave()
	else:
		ChangeState("Wait")
		# TODO 友好的界面切换效果
		pass
			
def onNetGameOver(msg):
	global State, thisHid, scr_play
	if State == "Play":
		if msg.winHid == thisHid:
			scr_play.OnGameOver(0)
			Global.API.show_msg("你赢了")
		else:
			scr_play.OnGameOver(1)
			Global.API.show_msg("你输了")
	ChangeState("Wait");
			
def onNetThisPrepBubs(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThisPrepBubs(ChessHelper.StrToColors(msg.colors))
	
def onNetThisMove(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThisMove(msg.isOK)

def onNetThisRemove(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThisRemove(msg.isOK, msg.score)

def onNetThisPutBubs(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThisPutSlots(ChessHelper.StrToPoss(msg.positions))


def onNetThatPrepBubs(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThatPrepBubs(ChessHelper.StrToColors(msg.colors))
		

def onNetThatMove(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThatMove(ChessHelper.StrToMove(msg.points))

		
def onNetThatRemove(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThatRemove(ChessHelper.StrToRemoves(msg.lineInfo), msg.score)
	

def onNetThatPutBubs(msg):
	global State, scr_play
	if State == "Play":
		scr_play.OnNetThatPutBubs(ChessHelper.StrToPoss(msg.positions))
		
	
# =========================================================
# 供Flash调用
# =========================================================
def Train():
	global scr_wait
	scr_wait.OnTrainClicked()
	
def SetReady(isReady):
	global scr_wait
	print("UI:"+str(isReady))
	scr_wait.OnReadyClicked(isReady)

def RequestLeaveRoom():
	Bufan_init.onClose(None)

def Break():
	global scr_play
	Global.Sender.cs_reqBreak()
	













	
	
	
	
	