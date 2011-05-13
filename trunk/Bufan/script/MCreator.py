import iworld2d
import flash
# ��Ϸý�崴��


# ��������ʾͼƬ
def CreateImage(path, posX, poxY, scaleX, scaleY):
	image = iworld2d.image2d(path);
	image.pos = (posX, posY);
	image.scale = (scaleX, scaleY);
	image.brint_to_front();
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
def CreateMovie(path):	// TODO ??
	movie = flashui.movie(path, False, True, flashui.SM_NoScale);
	movie.enable_keyboard = False;
	timeout = None;
	
