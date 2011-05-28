import log

Room = None
MsgMgr = None
GameMgr = None

def init(room):
	global Room, MsgMgr
	Room = room
	MsgMgr = Room.MsgMgr
	
def WriteLog(msg):
	log.info(msg)