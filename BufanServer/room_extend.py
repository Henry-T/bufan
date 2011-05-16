# -*- coding:GBK -*-

import hall_callback
import sdk_version

import bufan_room
import bufan_msg


event_callback = {
	# 消息处理映射
	'cs_req_leave': bufan_room.BufanRoom.onReqLeaveRoom,
	'cs_set_positon': bufan_room.BufanRoom.onSetPos,
	}
	
def init():
	global event_callback
	### 设置游戏房间的 消息定义 和 消息回调函数
	hall_callback.register_game_room_msgdefine_and_callback(\
		bufan_msg.MsgDefine, event_callback)

	### 设置房间类的定义
	hall_callback.set_class_define(
			{ ### 游戏模式: (最小人数, 最大人数, 类, 模式名称) 
				1: (2, 2, bufan_room.BufanRoom, "单人模式", 0),
			} 
	)


## 使用公共大厅
hall_callback.use_hall(sdk_version.SDK_VERSION_1_0)
### 设置初始化函数
hall_callback.init = init

