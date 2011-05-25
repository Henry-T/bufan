# iTownSDK �ṩ��ý�崴����ʾ���ŵȹ���
#������ѡ����Ϸ����Ҫ�õ��Ľ��м򵥷�װ

import iworld2d
import flashui
# ��Ϸý�崴��

def initial():
	iworld2d.init()
	

# ��������ʾͼƬ
def CreateImage(path, posX, posY, scaleX, scaleY):
	image = iworld2d.image2d(path);
	image.pos = (posX, posY);
	image.scale = (scaleX, scaleY);
	image.bring_to_front();
	return image;

# ��������ʾģ��
def CreateModel2D(path, seqName, posX, posY):
	model = iworld2d.model2d(path, seqName);
	model.pos = (posX, posY);
	return model;
	
# ��������ʾ����
def CreateParticle(path, posX, posY):
	particle = iworld2d.particle2d(path);
	particle.pos = (posX, posY);
	return particle;
	
# ����ӰƬ
def CreateMovie(path):	# TODO ??
	movie = flashui.movie(path, False, True, flashui.SM_NoScale);
	movie.enable_keyboard = False;
	timeout = None;
	
