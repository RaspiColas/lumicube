# Include pong.py, rubik.py, lavalamp.py, lumi8queens.py, newlife.py, and digitalrain.py from the Desktop directory
# Note: Be carefull with global definitions in the individual scripts later included scripts could overwrite them
# This way all foundry-api items are available to the included scripts
# By N.Mercouroff aka Raspicolas, 2022

script=open('pong.py').read()
exec(script)

script=open('rubik.py').read()
exec(script)

script = open('lavalamp.py').read()
exec(script)

script = open('lum8queens.py').read()
exec(script)

script = open('newlife.py').read()
exec(script)

script = open('digitalrain.py').read()
exec(script)

i = 0
while True:
	pong()
	rubik()
	lavalamp()
	lum8queens()
	life()
	digitalrain()
	i += 1
	print('loop nb %s' %(i))
