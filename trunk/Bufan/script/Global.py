import iapi
import iworld2d
import cg_sound


API = None
Sender = None
Sound = None


def init():
	global API, Sender, Sound
	iworld2d.init()
	cg_sound.init()
	
	API = iapi.API()
	Sender = API.sender
	Sound = cg_sound
	
def Destroy():
	iworld2d.destroy()
	cg_sound.destroy()
