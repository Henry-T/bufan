MsgDefine = {
	# ===========================================
	# 游戏状态消息
	# ===========================================
	# 欢迎信息
	"sc_welcome":{"chid":"I"},
	# 发送玩家数据
	"sc_player_info":{'nickname':'s','hid':'I','win':'I', 'lose':'I', 'draw':'I', 'breakC':'I'},
	# 客户端准备状态更改
	"cs_setReady":{"isReady":"i"},
	# 客户端请求离开
	"cs_req_leave":{},
	# 客户端离开
	"sc_playerLeft":{"chid":"I"},
	
	# ===========================================
	# 游戏逻辑消息
	# 每次收到客户端的逻辑操作后，剥夺其操作权
	# 服务端回发某些验证结果时，捎带授予操作权
	# ===========================================
	# 准备棋子 s的长度是棋子的数量
	"sc_prepBubs":{'colors':'s'},
	# 移动 四个char，分别代表StartX，StartY，EndX，EndY
	"cs_move":{'sX':'i', 'sY':'i', 'eX':'i', 'eY':'i'},
	# 消除 lineInfo 依次是起点终点对的xy坐标，4个长度一组
	"cs_remove":{"lineCount":'i', "lineInfo":'s'},
	# 放置棋子 放置棋子数量是positions的长度除以2
	"sc_pubBubs":{'positons':'s'},
}