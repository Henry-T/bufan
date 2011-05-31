# iTownSDK 提供了媒体创建显示播放等功能
#　这里选择游戏中需要用到的进行简单封装

import iworld2d
import flashui
# 游戏媒体创建

SlotLayer = 2
BGLayer = -1

def initial():
	pass
	

# 创建并显示图片
def CreateImage(path, posX, posY, scaleX, scaleY, layer):
	image = iworld2d.image2d(path, "", layer);
	image.pos = (posX, posY);
	image.scale = (scaleX, scaleY);
	image.bring_to_front();
	return image;

# 创建并显示模型
def CreateModel2D(path, seqName, posX, posY):
	model = iworld2d.model2d(path, seqName);
	model.pos = (posX, posY);
	return model;
	
# 创建并显示粒子
def CreateParticle(path, posX, posY):
	particle = iworld2d.particle2d(path);
	particle.pos = (posX, posY);
	return particle;
	
# 创建影片
def CreateMovie(path):
	movie = flashui.movie(path, False, True, flashui.SM_NoScale)
	movie.align = flashui.Align_BottomCenter
	movie.enable_keyboard = False # ui层不接收键盘消息
	return movie
	
