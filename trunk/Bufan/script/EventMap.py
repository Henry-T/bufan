# ÓÎÏ·ÏûÏ¢Ó³Éä
import InGame

eventMap = {}

def GetEventMap():
	if not eventMap:
		# eventMap["cs_req_leave"] = InGame.onReqLeaveRoom #
		eventMap["sc_get_score"] = InGame.onGetScore
	return eventMap