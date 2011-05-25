import BufanRoom

EventMap = {
	"cs_setReady'":BufanRoom.BufanRoom.onSetReady,
	"cs_req_leave": BufanRoom.BufanRoom.onReqLeaveRoom,
	
	"cs_move":BufanRoom.BufanRoom.onMove,
	"cs_remove":BufanRoom.BufanRoom.onRemove,
	}