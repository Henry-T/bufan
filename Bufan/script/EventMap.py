# ÓÎÏ·ÏûÏ¢Ó³Éä
import InGame

eventMap = {}

def GetEventMap():
	if not eventMap:
		eventMap["sc_get_score"] = InGame.onGetScore
	return eventMap