import iapi


API = None
Sender

def init():
	global API, Sender
	API = iapi.API()
	Sender = API.sender
