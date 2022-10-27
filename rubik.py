# Semi-Rubik cube on the lumicube (semi because there are only 3 rubik_faces).
# It fills the rubik_faces with blue, red, and green, then try to solve it randomly
# You can adjust the speed and the number of trials by adjusting delay (in sec) and i_max
# By N.Mercouroff aka Raspicolas, 2022

import time 
import random 

RUBIK_DELAY = 0.5
RUBIK_DURATION = 30

colors_name = [red, green, blue, orange, yellow, white]
leds = {}

# ====== RUBIK functions ========

rubik_faces = {}

def rubik_fill_face(f):
	global rubik_faces

	for i in range(3):
		for j in range(3):
			color = colors_name[random.randint(0, len(colors_name) - 1)]
			rubik_faces [f, i, j] = color

	faces_color = colors_name[0:3]
	random.shuffle(faces_color)
	rubik_faces [f, 1, 1] = faces_color[f]	# Forces each face to have a central color different

	return

def rubik_draw_face(f):
	leds = {}
	for i in range(3):
		for j in range(3):
			color = rubik_faces[f, i, j]
			leds[i*3 + 8 * (f % 2), j*3 + 8 * (f//2)] = color
			leds[i*3 + 1 + 8 * (f % 2), j*3 + 8 * (f//2)] = color
			leds[i*3 + 8 * (f % 2), j*3+1 + 8 * (f//2)] = color
			leds[i*3 + 1 + 8 * (f % 2), j*3+1 + 8 * (f//2)] = color
	display.set_leds(leds)
	return


def rubik_rotate_face(f, direction):
	c1 = rubik_faces[f, 0, 0]
	c2 = rubik_faces[f, 0, 1]
	c3 = rubik_faces[f, 0, 2]
	c4 = rubik_faces[f, 1, 2]
	c5 = rubik_faces[f, 2, 2]
	c6 = rubik_faces[f, 2, 1]
	c7 = rubik_faces[f, 2, 0]
	c8 = rubik_faces[f, 1, 0]

	if direction == 1:
		rubik_faces[f, 0, 0] = c7
		rubik_faces[f, 0, 1] = c8
		rubik_faces[f, 0, 2] = c1
		rubik_faces[f, 1, 2] = c2
		rubik_faces[f, 2, 2] = c3
		rubik_faces[f, 2, 1] = c4
		rubik_faces[f, 2, 0] = c5
		rubik_faces[f, 1, 0] = c6
	else:
		rubik_faces[f, 0, 0] = c3
		rubik_faces[f, 0, 1] = c4
		rubik_faces[f, 0, 2] = c5
		rubik_faces[f, 1, 2] = c6
		rubik_faces[f, 2, 2] = c7
		rubik_faces[f, 2, 1] = c8
		rubik_faces[f, 2, 0] = c1
		rubik_faces[f, 1, 0] = c2

	if f == 0:
		rubik_faces[1, 0, 0], rubik_faces[2, 2, 0] = rubik_faces[2, 2, 0], rubik_faces[1, 0, 0]
		rubik_faces[1, 0, 1], rubik_faces[2, 1, 0] = rubik_faces[2, 1, 0], rubik_faces[1, 0, 1]
		rubik_faces[1, 0, 2], rubik_faces[2, 0, 0] = rubik_faces[2, 0, 0], rubik_faces[1, 0, 2]
	elif f == 1:
		rubik_faces[0, 2, 0], rubik_faces[2, 2, 0] = rubik_faces[2, 2, 0], rubik_faces[0, 2, 0]
		rubik_faces[0, 2, 1], rubik_faces[2, 2, 1] = rubik_faces[2, 2, 1], rubik_faces[0, 2, 1]
		rubik_faces[0, 2, 2], rubik_faces[2, 2, 2] = rubik_faces[2, 2, 2], rubik_faces[0, 2, 2]
	elif f == 2:
		rubik_faces[0, 0, 2], rubik_faces[1, 0, 2] = rubik_faces[1, 0, 2], rubik_faces[0, 0, 2]
		rubik_faces[0, 1, 2], rubik_faces[1, 1, 2] = rubik_faces[1, 1, 2], rubik_faces[0, 1, 2]
		rubik_faces[0, 2, 2], rubik_faces[1, 2, 2] = rubik_faces[1, 2, 2], rubik_faces[0, 2, 2]

	return


def rubik(duration=RUBIK_DURATION, delay=RUBIK_DELAY):

	display.set_all(black)
	time.sleep(delay)

	for f in range(3):
		rubik_fill_face(f)
		rubik_draw_face(f)

	t0 = time.time()

	while (duration == 0) or (time.time() - t0 < duration):
		time.sleep(delay)
		f = random.randint(0, 2)
		direction = random.randint (0, 1) * 2 - 1
		rubik_rotate_face(f, direction)
		rubik_draw_face(0)
		rubik_draw_face(1)
		rubik_draw_face(2)

	return

# ====== RUBIK main ========

if __name__ == '__main__':
	rubik()
