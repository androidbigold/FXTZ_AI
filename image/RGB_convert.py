from PIL import Image
import os       

path = './' #path是图片所在的文件夹


def changeMode(path):
	for file in os.listdir(path):
		full_path = os.path.join(path, file)
		if os.path.isdir(full_path):
			changeMode(full_path)

		extension = file.split('.')[-1]
		filename = file.split('.')[0]
		if extension == 'bmp':
			img = Image.open(full_path)
			if img.mode != 'RGB':
				img_RGB = img.convert('RGB')
				img_RGB.save(os.path.join(path, filename) + '.jpg')
				os.remove(full_path)


if __name__ == '__main__':
	changeMode(path)
