# 游戏消息映射
import GameManager

EventMap = {
	"sc_welcome":GameManager.onNetWelcome,
	"sc_playerInfo":GameManager.onNetPlayerInfo,
	"sc_playerReady":GameManager.onNetPlayerReady,
	"sc_playerLeft":GameManager.onNetPlayerLeft,
	"sc_gameOver":GameManager.onNetGameOver,
	
	"sc_this_prepBubs":GameManager.onNetThisPrepBubs,
	"sc_this_move":GameManager.onNetThisMove,
	"sc_this_remove":GameManager.onNetThisRemove,
	"sc_this_putBubs":GameManager.onNetThisPutBubs,
	
	"sc_that_prepBubs":GameManager.onNetThatPrepBubs,
	"sc_that_move":GameManager.onNetThatMove,
	"sc_that_remove":GameManager.onNetThatRemove,
	"sc_that_putBubs":GameManager.onNetThatPutBubs,
}



# eventMap = {}

# def GetEventMap():
	# # 官方例子中缺少这一行
	# global eventMap
	# if not eventMap:
		# eventMap["sc_welcome"] = GameManager.onGetWelcome
		# eventMap["sc_player_info"] = GameManager.onGetPlayerInfo
	# return eventMap