from random import randint

srt = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
print("Note \n............Score = 100\nFor each wrong answer -10 will be deducted")
x = randint(srt, end)

score = 100
def start():
	u_in = int(input("Try your guess: "))
	if u_in == x:
		print("Congrats your guess was correct!!!")

	elif u_in != x:
		global score
		score -= 10
		print("Wrong guess\n.............score= %d \nTry again"%(score))
		if score < 30:
			print("Sorry your score is less than 30 ...Want to get help? or quit (h/q)")
			prompt = input()
			if prompt == 'h':
				temp = x % u_in
				sempp = x / u_in
				print("Your choice is %d multiplication and %d addition times away from the last input" % (sempp, temp))
				u_in = int(input("Did you figured it out?\n Enter again..."))
				if u_in == x:
					print("Congrats your guess was correct!!!")
					exit()
				else:
					print("Sorry Game over")
					exit()
			elif prompt == 'q':
				exit()
		start()




start()





