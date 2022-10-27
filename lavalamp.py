# Generate a lava lamp effect using OpenSimplex noise.
# By Abstract Foundry, 2022
# Adapted by N.Mercouroff for inclusion in main anumations

import time, random

LAVA_DELAY = 1/30
LAVA_DURATION = 30


# ====== LAVALAMP functions ========

def lava_colour(x, y, z, t):
    scale = 0.10
    speed = 0.05
    hue = noise_4d(scale * x, scale * y, scale * z, speed * t)
    return hsv_colour(hue, 1, 1)

def lava_paint_cube(t):
    colours = {}
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x == 8 or y == 8 or z == 8:
                    colour = lava_colour(x, y, z, t)
                    colours[x,y,z] = colour
    display.set_3d(colours)


def lavalamp(duration=LAVA_DURATION, delay=LAVA_DELAY):
	t = random.randint(0, 10000)
	t0 = time.time()

	while (duration == 0) or (time.time() - t0 < duration):
		lava_paint_cube(t)
		time.sleep(delay)
		t += 1
	
	return

# ====== LAVALAMP main ========

if __name__ == '__main__':
	lavalamp()
