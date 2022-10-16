# Bouncing pixels on the lumicube.
# You can adjust the number of pixels with pixel_nb
# By N.Mercouroff aka Raspicolas, 2022

import random, time

delay = 0.02
pixel_nb = 5
iteration_nb = 128

def bounce(x, vx):
	x += vx
	if x >= 16:
		x = 30 - x
		vx = -vx
	elif x < 0:
		x = -x
		vx = -vx
	return x, vx


def next_pixel(pixel, vector):
	x, y = pixel
	vx, vy = vector
	x1, vx = bounce(x, vx)
	y1, vy = bounce(y, vy)

	if x1>= 8 and y1 >= 8:
		if x < 8:
			(x1, y1) = (y1, 15 -x1)
			(vx, vy) = (vy, -vx)
		if y < 8:
			(x1, y1) = (15 - y1, x1)
			(vx, vy) = (-vy, vx)

	return (x1, y1), (vx, vy)


def interate_color(c):
	pixel = pixels[c]
	x = pixel['x']
	y = pixel['y']
	vx = pixel['vx']
	vy = pixel['vy']
	x0 = pixel['x0']
	y0 = pixel['y0']
	color = pixel['color']

	(x1, y1), (vx1, vy1) = next_pixel((x, y), (vx, vy))
	display.set_led(x0, y0, black)
	display.set_led(x1, y1, color)
	pixel['x'] = x1
	pixel['y'] = y1
	pixel['vx'] = vx1
	pixel['vy'] = vy1
	pixel['x0'] = x
	pixel['y0'] = y

	return

colors = [red, orange, green, blue, yellow]

while True:
	i = 0
	pixels = {}
	for c in range(pixel_nb):
		pixels[c] = {
			'color': colors[c % len(colors)],  #hsv_colour(random.random(), 1, 1),
			'x': random.randint(0, 7) + c%2 * 8,
			'y': random.randint(0, 7) + c%3 * 8,
			'vx': random.randint(0, 1)*2 - 1,
			'vy': random.randint(0, 1)*2 - 1,
			'x0': 0,
			'y0': 0
		}

	display.set_all(black)

	while i < iteration_nb:
		for c in range(pixel_nb):
			interate_color(c)
			time.sleep(delay)
		i += 1

