# Bouncing pixels on the lumicube.
# You can adjust the number of pixels with pong_pixel_nb
# By N.Mercouroff aka Raspicolas, 2022

import random, time

PONG_DELAY = 0.1
PONG_DURATION = 30

colors_value = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

leds = {}

# ====== PONG functions ========

pong_pixel_nb = 6

def pong_bounce(x, vx):
	""" 
		Returns the new coordinate and vector after bouncing
	"""
	x += vx
	if x >= 16:
		x = 30 - x
		vx = -vx
	elif x < 0:
		x = -x
		vx = -vx
	return x, vx


def pong_next_pixel(pixel, vector):
	""" 
		Returns the next pixel coordinates and vector  
	"""
	x, y = pixel
	vx, vy = vector
	x1, vx = pong_bounce(x, vx)
	y1, vy = pong_bounce(y, vy)

	if x1>= 8 and y1 >= 8:
		if x < 8:
			(x1, y1) = (y1, 15 -x1)
			(vx, vy) = (vy, -vx)
		if y < 8:
			(x1, y1) = (15 - y1, x1)
			(vx, vy) = (-vy, vx)

	return (x1, y1), (vx, vy)


def pong_iterate_pixel(c):
	""" 
		Iterates and displays the pixel number c
	"""
	global leds

	pixel = pixels[c]
	x0 = pixel['x0']
	y0 = pixel['y0']
	x1 = pixel['x1']
	y1 = pixel['y1']
	x2 = pixel['x2']
	y2 = pixel['y2']
	vx = pixel['vx']
	vy = pixel['vy']
	color = pixel['color']

	(x3, y3), (vx1, vy1) = pong_next_pixel((x2, y2), (vx, vy))

	leds[x0, y0] = hsv_colour(color, 1, 0)
	leds[x1, y1] = hsv_colour(color, 1, 0.3)
	leds[x2, y2] = hsv_colour(color, 1, 0.6)
	leds[x3, y3] = hsv_colour(color, 1, 1)

	pixel['x0'] = x1
	pixel['y0'] = y1
	pixel['x1'] = x2
	pixel['y1'] = y2
	pixel['x2'] = x3
	pixel['y2'] = y3
	pixel['vx'] = vx1
	pixel['vy'] = vy1

	return


def pong(duration=PONG_DURATION, delay=PONG_DELAY):
	global pixels, leds

	pixels = {}
	i = 0
	for c in range(pong_pixel_nb):
		panel = c % 3	# panel = 0 is front, panel = 1 is side, panel = 2 is top
		x = random.randint(0, 7) + (panel % 2) * 8
		y = random.randint(0, 7) + (panel // 2) * 8
		vx = random.randint(0, 1)*2 - 1
		vy = random.randint(0, 1)*2 - 1

		pixels[c] = {
			'color': colors_value[c % len(colors_value)],  # if some fantasy in color is allowed, you can try that: hsv_colour(random.random(), 1, 1),
			'x0': x,
			'y0': y,
			'x1': x,
			'y1': y,
			'x2': x,
			'y2': y,
			'vx': vx,
			'vy': vy
		}
	display.set_all(black)

	t0 = time.time()

	while (duration == 0) or (time.time() - t0 < duration):
		leds = {}
		for c in range(pong_pixel_nb):
			pong_iterate_pixel(c)
		
		display.set_leds(leds)
		time.sleep(delay)

	return

# ====== PONG main ========

if __name__ == '__main__':
	pong()
