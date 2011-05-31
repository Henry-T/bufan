import iapi
import iworld2d


API = None
Sender = None


def init():
	global API, Sender
	iworld2d.init()
	API = iapi.API()
	Sender = API.sender
	
def Destroy():
	iworld2d.destroy()
