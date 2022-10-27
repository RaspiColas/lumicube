# Yet Another Game of Life variant.
# Conway's Game of Life (https://en.wikipedia.org/wiki/Conway's_Game_of_Life).
# modified to show new cells as green, old cells as blue, new dead cell as red
# will run for as long as 5 minutes, automatically checking for stopped or loop states, when it will pause for a few seconds then restart
# Author : Kevin Haney
# Date : 10/9/2022
# Version : 1.0
# Adapted by N.Mercouroff for inclusion in main anumations

import random

# fresh = hsv_colour(0.3, 1, 1)   # green
# old = hsv_colour(0.6, 1, 0.8)   # blue
# dying = hsv_colour(0.15, 1, 0.6)    # yellow
# dead = hsv_colour(0.0, 1, 0.4)  # red

LIFE_DELAY = 0.2
LIFE_DURATION = 60


def life(duration=LIFE_DURATION, delay=LIFE_DELAY):

	t0 = time.time()

	while True:

		fresh = hsv_colour(random.random(), 1, 1)   # green
		old = hsv_colour(random.random(), 1, 0.7)   # blue
		dying = hsv_colour(random.random(), 1, 0.4)    # yellow
		dead = hsv_colour(random.random(), 1, 0.1)  # red

		max_turns = 300

		starting_live_ratio = 0.4
	#    colour = random_colour()
		colour = fresh
		num_turns = 0
		alive_cells = []
		for x in range(0, 16):
			for y in range(0, 16):
				if x < 8 or y < 8:
					if random.random() < starting_live_ratio:
						alive_cells.append((x, y))

		def num_alive_neighbours(x, y):
			num_neighbours = 0
			for x2 in [x-1, x, x+1]:
				for y2 in [y-1, y, y+1]:
					if (x2, y2) != (x, y):
						neighbour = (x2, y2)
						# Account for 3D nature of panels
						if x2 == 8 and y2 >= 8:
							neighbour = (y2, 7)
						elif y2 == 8 and x2 >= 8:
							neighbour = (7, x2)
						if neighbour in alive_cells:
							num_neighbours += 1
			return num_neighbours

		leds = {}
		last_cells = []  # keep track of last state for when things stop changing
		prev_cells = []  # keep track of two states ago go catch when we're stuck in a repeating loop
		loop_waits = 0

		while (num_turns < max_turns):
			next_cells = []
			prev_cells = last_cells
			last_cells = alive_cells
			prev_leds = leds
			leds = {}
			for x in range(0, 16):
				for y in range(0, 16):
					if x < 8 or y < 8:
						alive = (x, y) in alive_cells
						neighbours = num_alive_neighbours(x, y)
						# Remains alive
						if alive and (neighbours == 2
                                                        or neighbours == 3):
							next_cells.append((x, y))
							leds[x, y] = old  # colour
						# Becomes alive
						elif not alive and neighbours == 3:
							next_cells.append((x, y))
							leds[x, y] = fresh  # colour
						# Else dead
						else:
							if alive:
								k = x, y
								if prev_leds.get((x, y)) == old:
									leds[x, y] = dead
								else:
									leds[x, y] = dying
							else:
								leds[x, y] = black
			display.set_leds(leds)
			alive_cells = next_cells
			if (alive_cells == last_cells):
				time.sleep(delay)
				break
			if (alive_cells == prev_cells):
				loop_waits += 1
				if (loop_waits > 20):
					loop_waits = 0
					break
			time.sleep(delay)
			if (duration != 0) and (time.time() - t0 > duration):
				return
			num_turns += 1


if __name__ == '__main__':
	life()
