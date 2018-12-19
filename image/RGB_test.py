from PIL import Image     
import os       

path = './' #path是图片所在的文件夹

def checkMode(path):
	for file in os.listdir(path):
		full_path = os.path.join(path, file)
		if os.path.isdir(full_path):
			checkMode(full_path)

		extension = file.split('.')[-1]
		if extension == 'bmp':
			img = Image.open(full_path)
			print(full_path + ', ' + img.mode)


if __name__ == '__main__':
	checkMode(path)
