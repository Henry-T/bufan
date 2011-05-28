import iapi


API = None
Sender = None

def init():
	global API, Sender
	API = iapi.API()
	Sender = API.sender
