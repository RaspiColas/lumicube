# A script to solve the problem of the 8 queens on the lumicube
# Each time a solution is found, a new face is used to look for next solution
# Speed can be adjusted with the DELAY, 
# Duration of the animation with DURATION (0 is till all solutions are found)
# By N.Mercouroff aka Raspicolas, 2022

import time

QUEENS_DELAY = 0.02
QUEEN_DURATION = 60
QUEEN_INFINITE = False

queens = {}
nb_sol = 0

a = 'abcdefgh'

draw_iter = True
index = 0
x_d = [0, 8, 0]
y_d = [0, 0, 8]
colors_name = [red, green, blue, orange, yellow]
c = 0
color = colors_name[c]
t0 = time.time()
duration_value = 0
delay_value = QUEENS_DELAY


def init_echiquier(echiquier):
	for i in range (8):
		echiquier[i] = {}
		for j in range(8):
			echiquier[i,j] = False
	return


def copie_echiquier(echiquier1, echiquier):
	for i in range(8):
		echiquier[i] = {}
		for j in range(8):
			echiquier[i, j] = echiquier1[i,j]
	return


def fill_queen(x,y, echiquier1):
	echiquier= {}
	copie_echiquier(echiquier1, echiquier)
	for i in range(8):
		echiquier[x,i] = True
		echiquier[i,y] = True
	i = x
	j = y
	while (i > 0) and (j > 0):
		i -= 1
		j -= 1
		echiquier[i,j] = True
	i = x
	j = y
	while (i > 0) and (j < 7):
		i -= 1
		j += 1
		echiquier[i, j] = True
	i = x
	j = y
	while (i < 7) and (j < 7):
		i += 1
		j += 1
		echiquier[i, j] = True
	i = x
	j = y
	while (i < 7) and (j > 0):
		i += 1
		j -= 1
		echiquier[i, j] = True
	return echiquier


def first_queen(x, echiquier):
	for i in range(8):
		if not echiquier[x,i]:
			return(i)
	return(-1)


def next_level(i, echiquier):
	global nb_sol, index, color, c

	if (duration_value != 0) and (time.time() - t0 > duration_value):
		return

	if i == 8:
		nb_sol += 1
		msg = "Sol %s:" % (nb_sol)
		for j in range(8):
			msg = msg + " " + a[j] + str(queens[j]+1)
		print(msg)
		display_sol()
		display_echiquier()

		index = (index + 1) % 3
		c = (c + 1) % len(colors_name)
		color = colors_name[c]
		return 
	for j in range(8):
		if not echiquier[i,j]:
			echiquier1 = fill_queen(i,j,echiquier)
			queens[i] = j
			if draw_iter:
				display_echiquier()
			next_level(i+1, echiquier1)
			queens[i] = None
			if draw_iter:
				display_echiquier()
	return


def display_echiquier():
	leds = {}
	for i in range(8):
		for j in range(8):
			leds[i+x_d[index], j+y_d[index]] = black
			try:
				if queens[i] == j:
					leds[i+x_d[index], j+y_d[index]] = color
			except:
				continue
	display.set_leds(leds)
	time.sleep(delay_value)
	return


def display_sol():
	leds = {}
	for i in range(8):
		for j in range(8):
			leds[i+x_d[index], j+y_d[index]] = black
			try:
				if queens[i] == j:
					leds[i+x_d[index], j+y_d[index]] = white
			except:
				continue
	display.set_leds(leds)
	time.sleep(10*delay_value)
	return


def lum8queens(duration=QUEEN_DURATION, delay=QUEENS_DELAY):
	global duration_value, delay_value

	duration_value = duration
	delay_value = delay
	echiquier = {}
	display.set_all(black)
	init_echiquier(echiquier)
	next_level(0, echiquier)
	return


if __name__ == "__main__":
	while True:
		lum8queens()
		if not QUEEN_INFINITE:
			break
