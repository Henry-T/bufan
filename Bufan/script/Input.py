# ������Ϣ֧��ģ��
import game

def IsLeftClicked(buttonState, button):
	if buttonState == game.MSG_MOUSE_UP:
		if button == game.MOUSE_BUTTON_LEFT:
			return 1
	return 0
	
	