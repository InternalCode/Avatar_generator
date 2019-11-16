import random, time, threading, os
from PIL import Image
class Avatar():
	def __init__(self):
		
		print('Avatar generator\n=======================================================')
		try:
			avatar_size = int(input('Avatar size\nstandard value is 7: '))
		except ValueError:
			avatar_size = 7
		if avatar_size == 0:
			avatar_size = 7
		try:
			avatar_scale = int(input('Avatar Scale\nstandard value is 7: '))
		except ValueError:
			avatar_scale = 7
		if avatar_scale == 0:
			avatar_scale = 7
		try:
			avatars_to_generate = int(input('Quantity: '))
		except ValueError:
			avatars_to_generate = 1
		colors = input('Random colors Y/N: ')
		colors = colors.lower()		
		if colors == '' or colors != 'n' or colors != 'n':
			colors = 'y'
		print('=======================================================')
		
		for i in range(avatars_to_generate):
			avatar_array = []
			print('Generating... nr', i + 1)
			self.create_array(avatar_array, avatar_size)
			# ~ self.display_array(avatar_array)
			self.generate_avatar(avatar_array, avatar_size)
			# ~ self.display_array(avatar_array)
			self.mirror_avatar(avatar_array, avatar_size)
			# ~ self.display_array(avatar_array)
			avatar_array = self.interpolation(avatar_array, avatar_scale)
			# ~ self.display_array(avatar_array)
			self.image_generate(avatar_array, colors)
					
	def create_array(self, array, size):
		for y in range(size):
			array.append([])
			for x in range(size):
				array[y].append('_')
		return None
		
	def display_array(self, array):
		print('\n')
		for y in range(len(array)):
			print(array[y])
		return None
		
	def generate_avatar(self, array, size):
		for y in range(size):
			for x in range(size):
				r = random.randint(0, 100)
				if r > 50:
					array[y][x] = 'x'
		return None

	def mirror_avatar(self, array, size):
		mirror = size // 2
		for y in range(size):
			for x in range(mirror):
				array[y][x] = array[y][(size - 1) - x]
		return None
		
	def interpolation(self, array, inter):
		array2 = []
		array3 = []
		for y in range(len(array)):
			array2.append([])
			for x in range(len(array[y])):
				for i in range(inter):
					array2[y].append(array[y][x])
		for y in range(len(array2)):
			for i in range(inter):
				array3.append(array2[y])
		del array
		del array2
		return array3[:]

	def image_generate(self, array, colors):
		if colors == 'y':
			color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
		else:
			color = (255,255,255)
		image_obj = Image.new('RGBA', (len(array), len(array)), (0,0,0,0))
		for y in range(len(array)):
			for x in range(len(array)):
				if array[y][x] == 'x':
					image_obj.putpixel((x,y), (color))
		f_name = ('%s.png' %(str(int(time.time()))))
		image_obj.save(f_name)
		image_obj.close()
		time.sleep(1)
		return None
		
if __name__ == '__main__':
	ava = Avatar()
