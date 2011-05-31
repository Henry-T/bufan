import room_extend

# 函数定义要写在调用之前
def OnNetSetReady(room,player, msg):
	room.onNetSetReady(player, msg)
def OnNetReqLeave(room, player, msg):
	room.onNetReqLeaveRoom(player, msg)
def OnNetReqBreak(room, player, msg):
	room.onNetReqBreak(player,msg)
def OnNetMove(room,player, msg):
	room.onNetMove(player, msg)
def OnNetReqPut(room, player, msg):
	room.onNetReqPut(player, msg)
def OnNetRemove(room,player, msg):
	room.onNetRemove(player, msg)
	
EventMap = {
	"cs_setReady":OnNetSetReady,
	"cs_reqLeave": OnNetReqLeave,
	"cs_reqBreak": OnNetReqBreak,
	"cs_this_move":OnNetMove,
	"cs_this_reqPut":OnNetReqPut,
	"cs_this_remove":OnNetRemove,
	}
	
	