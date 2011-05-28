# 客户端每次行动后都挂起，等待服务器发回确认消息后继续行动

MsgDefine = {
	# ===========================================
	# 游戏状态消息
	# ===========================================
	# 欢迎信息
	"sc_welcome":{"chid":"I"},
	# 发送玩家数据
	"sc_playerInfo":{'nickname':'s','hid':'I','win':'I', 'lose':'I', 'draw':'I', 'breakC':'I'},
	# 客户端准备状态更改
	"cs_setReady":{"isReady":"i"},
	# 状态更改确认
	"sc_playerReady":{"hid":"i", "isReady":"i"},
	# 客户端请求离开
	"cs_reqLeave":{},
	# 客户端离开
	"sc_playerLeft":{"chid":"I"},
	
	# ===========================================
	# 游戏逻辑消息 - 自方
	# 每次收到客户端的逻辑操作后，剥夺其操作权
	# 服务端回发某些验证结果时，捎带授予操作权
	# ===========================================
	# 准备棋子 s的长度是棋子的数量
	"sc_this_prepBubs":{'colors':'s'},
	# 移动 四个char，分别代表StartX，StartY，EndX，EndY
	"cs_this_move":{'sX':'i', 'sY':'i', 'eX':'i', 'eY':'i'},
	# 确认移动
	"sc_this_move":{},
	# 消除 lineInfo 依次是起点终点对的xy坐标，4个长度一组
	"cs_this_remove":{"lineInfo":'s'},
	# 确认消除
	"cs_this_remove":{}
	# 放置棋子 放置棋子数量是positions的长度除以2
	"sc_this_putBubs":{'positons':'s'},
	
	# ===========================================
	# 游戏逻辑消息 - 对方
	# 每次收到客户端的逻辑操作后，剥夺其操作权
	# 服务端回发某些验证结果时，捎带授予操作权
	# ===========================================
	# 准备棋子
	"sc_that_prepBubs":{"colors":"s"},
	# 移动棋子
	"sc_that_move":{"sX":"i", "sY":"i", "eX":"i", "eY":"i"},
	# 消除棋子
	"sc_that_remove":{"lineInfo":"s"},
	# 放置棋子
	"sc_that_putBubs":{"positions":"s"}
}