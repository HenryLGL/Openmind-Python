print "welcome to this great adventure!Choose the road to explore;there road #1 and road #2."
road = raw_input(">")

if road == "1" :
	print "There a monster waiting for you;excape,or beat it?"
	Choice = raw_input("excape or beat it? \n")
	if Choice == "excape" :
		print "The monster moves quickly and then it catches you!! "
	elif Choice == "beat it" :
		print "Unfortunately, you fall in a abyss and there is another adventure waiting for you."
	else:
		print "You are stunned and catched by the monster.."

elif road == "2" :
	print "You find a women crying beside a tree.help her or ignore?"		
	Action = raw_input("help her or ignore? \n")
	if Action == "help her" :
		print "Yes,you are a good man but unfortunately she is a ghost,and kill you,Hah!"
	elif Action == "ignore" :
		print "She follow you about 15 minutes but finally maybe turn back to the tree."
	else:
		print "You are stunned,and she come to you.Run or try to talk with her?."
		Reaction = raw_input("run or talk? \n")
		if Reaction == "run" :
			print "She is a ghost and catches you quickly!!!"
		elif Reaction == "talk" :
			print "Oh,she is your adventure partner."
		else :
			print "She kills you."
	