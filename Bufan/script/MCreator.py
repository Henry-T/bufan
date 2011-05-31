# iTownSDK �ṩ��ý�崴����ʾ���ŵȹ���
#������ѡ����Ϸ����Ҫ�õ��Ľ��м򵥷�װ

import iworld2d
import flashui
# ��Ϸý�崴��

SlotLayer = 2
BGLayer = -1

def initial():
	pass
	

# ��������ʾͼƬ
def CreateImage(path, posX, posY, scaleX, scaleY, layer):
	image = iworld2d.image2d(path, "", layer);
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
def CreateMovie(path):
	movie = flashui.movie(path, False, True, flashui.SM_NoScale)
	movie.align = flashui.Align_BottomCenter
	movie.enable_keyboard = False # ui�㲻���ռ�����Ϣ
	return movie
	
