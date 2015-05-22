from PIL import Image
import argparse

class FuckedImg(object):
	R, G, B = 0, 1, 2

	def __init__(self,path):
		self.im = Image.open(path)

	def killChannel(self,channel):
		source = list(self.im.split())
		source[channel] = source[channel].point(lambda i: i*0)
		source = tuple(source)
		return Image.merge(self.im.mode, source)

	def mirror(self):
	#reflects the right side of the image onto the left side
		sourcebox = (self.im.size[0]/2, 0, self.im.size[0], self.im.size[1])
		outbox = (0,0,self.im.size[0]/2,self.im.size[1])
		region = self.im.crop(sourcebox)
		region = region.transpose(Image.FLIP_LEFT_RIGHT)
		self.im.paste(region, outbox)
		return self.im


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", help="choose the file you'd like to glitch")
	parser.add_argument("-zc", "--ZapChannel", type=int, choices=[0, 1, 2], help="delete a color channel")
	parser.add_argument("-m", "--mirror", action="store_true", help="mirror image right to left")
	args = parser.parse_args()
	
	newImage = FuckedImg(args.filename)
	if args.ZapChannel:
		newImage.killChannel(int(args.ZapChannel)).show()
	if args.mirror:
		newImage.mirror().show()



if __name__ == "__main__":
	main()
