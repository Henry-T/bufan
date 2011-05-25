import log

Room = None

def init(room):
	global Room
	Room = room
	
def WriteLog(msg):
	log.info(msg)