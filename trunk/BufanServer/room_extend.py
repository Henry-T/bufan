# -*- coding:GBK -*-

import hall_callback
import sdk_version

import BufanRoom
import Message
import EventMap


	
def init():
	global event_callback
	### ������Ϸ����� ��Ϣ���� �� ��Ϣ�ص�����
	hall_callback.register_game_room_msgdefine_and_callback(\
		Message.MsgDefine, EventMap.EventMap)

	### ���÷�����Ķ���
	hall_callback.set_class_define(
			{ ### ��Ϸģʽ: (��С����, �������, ��, ģʽ����) 
				1: (2, 2, BufanRoom.BufanRoom, "����ģʽ", 0),
			} 
	)


## ʹ�ù�������
hall_callback.use_hall(sdk_version.SDK_VERSION_1_0)
### ���ó�ʼ������
hall_callback.init = init

	

