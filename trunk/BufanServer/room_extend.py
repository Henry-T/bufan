# -*- coding:GBK -*-

import hall_callback
import sdk_version

import bufan_room
import bufan_msg


event_callback = {
	# ��Ϣ����ӳ��
	'cs_req_leave': bufan_room.BufanRoom.onReqLeaveRoom,
	'cs_set_positon': bufan_room.BufanRoom.onSetPos,
	}
	
def init():
	global event_callback
	### ������Ϸ����� ��Ϣ���� �� ��Ϣ�ص�����
	hall_callback.register_game_room_msgdefine_and_callback(\
		bufan_msg.MsgDefine, event_callback)

	### ���÷�����Ķ���
	hall_callback.set_class_define(
			{ ### ��Ϸģʽ: (��С����, �������, ��, ģʽ����) 
				1: (2, 2, bufan_room.BufanRoom, "����ģʽ", 0),
			} 
	)


## ʹ�ù�������
hall_callback.use_hall(sdk_version.SDK_VERSION_1_0)
### ���ó�ʼ������
hall_callback.init = init

