import BufanRoom

EventMap = {
	"cs_setReady'":BufanRoom.BufanRoom.onNetSetReady,
	"cs_reqLeave": BufanRoom.BufanRoom.onNetReqLeaveRoom,
	
	"cs_this_move":BufanRoom.BufanRoom.onNetMove,
	"cs_this_remove":BufanRoom.BufanRoom.onNetRemove,
	}